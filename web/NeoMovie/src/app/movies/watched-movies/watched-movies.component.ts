import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AccountService, AlertService } from '@app/services';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-watched-movies',
  templateUrl: './watched-movies.component.html',
  styleUrls: ['./watched-movies.component.less']
})
export class WatchedMoviesComponent implements OnInit {

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
    this.accountService.getWatchedMovies(this.user.id)
    .pipe(first())
    .subscribe(
        (movies) => {
          if (Array.isArray(movies[0]))
            this.moviesList = movies
          else
            this.moviesList = [movies]
          console.log(movies);
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
