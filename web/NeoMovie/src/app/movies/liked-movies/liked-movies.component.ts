import { Component, OnInit } from '@angular/core';
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
    private alertService: AlertService
    ) {
    this.user = this.accountService.userValue;
}

  ngOnInit(): void {
    this.accountService.getLikedMovies(this.user.id)
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
