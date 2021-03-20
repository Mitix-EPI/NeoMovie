import { Component, OnInit } from '@angular/core';
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
    private alertService: AlertService
    ) {
    this.user = this.accountService.userValue;
}

  ngOnInit(): void {
    this.accountService.getWatchedMovies(this.user.id)
    .pipe(first())
    .subscribe(
        (movies) => {
            this.moviesList = movies
            console.log(movies);
        },
        (error) => {
            this.alertService.error(error);
        }
    );
  }

  goToMovie(movieId) {
    console.log('Clicked', movieId);
  }
}
