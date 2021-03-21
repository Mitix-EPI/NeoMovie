import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AccountService, AlertService } from '@app/services';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-liked-movies',
  templateUrl: './liked-movies.component.html',
  styleUrls: ['./liked-movies.component.less']
})
export class LikedMoviesComponent implements OnInit {

  user;
  moviesList = [];

  constructor(
    private accountService: AccountService,
    private alertService: AlertService,
    private router: Router
    ) {
    this.user = this.accountService.userValue;
}

  ngOnInit(): void {
    this.accountService.getLikedMovies(this.user.id)
    .pipe(first())
    .subscribe(
        (movies) => {
            if (Array.isArray(movies[0]))
              this.moviesList = movies
            else
              this.moviesList = [movies]
            console.log(this.moviesList);
        },
        (error) => {
            this.alertService.error(error);
        }
    );
  }

  goToMovie(movieId) {
    console.log('Clicked', movieId);
    this.router.navigate(['/movie', movieId]);
  }

  getImgUrl(movieTitle) {
    console.log("getImgUrl", movieTitle);
    const res = "url(../../assets/movies/" + movieTitle.toLowerCase().split(' ').join('-') + '.jpg)';
    console.log('Res', res);
    return res;
  }
}
