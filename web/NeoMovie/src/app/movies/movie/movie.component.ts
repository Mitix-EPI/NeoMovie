import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AccountService, AlertService } from '@app/services';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-movie',
  templateUrl: './movie.component.html',
  styleUrls: ['./movie.component.less']
})
export class MovieComponent implements OnInit {

  movieId;
  movie;
  movieLiked = false;
  movieWatched = false;

  constructor(
    private route: ActivatedRoute,
    private accountService: AccountService,
    private alertService: AlertService,
  ) { }

  ngOnInit(): void {
    const tag = document.createElement('script');

    tag.src = "https://www.youtube.com/iframe_api";
    document.body.appendChild(tag);
    this.movieId = this.route.snapshot.params['id'];
    this.accountService.getMovieById(this.movieId)
    .pipe(first())
    .subscribe(
        (movie) => {
            console.log("movie", movie);
            this.movie = movie
            this.accountService.isUserLikedMovies(this.movieId)
            .pipe(first())
            .subscribe(
                (isLiked) => {
                    this.movieLiked = isLiked
                },
                (error) => {
                    this.alertService.error(error);
                }
            );
        },
        (error) => {
            this.alertService.error(error);
        }
    );
  }

  getImgUrl(movieTitle) {
    const res = "../../assets/movies/" + movieTitle.toLowerCase().split(' ').join('-') + '.jpg';
    return res;
  }


  getVideoId(url) {
    console.log("GetVideoId", url);
    const res = url.replace("https://www.youtube.com/watch?v=", "");
    console.log("GetVideoId", res);
    return res;
  }

  watchMovie() {
    this.accountService.watchMovie(this.movieId)
    .pipe(first())
    .subscribe(
        (res) => {
            this.movieWatched = true;
        },
        (error) => {
            this.alertService.error(error);
        }
    );
  }

  likeMovie() {
    if (this.movieLiked == false) {
      this.accountService.likeMovie(this.movieId)
      .pipe(first())
      .subscribe(
          (res) => {
              this.movieLiked = true;
          },
          (error) => {
              this.alertService.error(error);
          }
      );
    } else {
      this.accountService.dislikeMovie(this.movieId)
      .pipe(first())
      .subscribe(
          (res) => {
              this.movieLiked = false;
          },
          (error) => {
              this.alertService.error(error);
          }
      );
    }
  }
}
