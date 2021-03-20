import { Component, OnInit } from '@angular/core';

import { AccountService } from '@app/services';
import { first } from 'rxjs/operators';
import { AlertService } from '../services/alert.service';

@Component({
    templateUrl: 'home.component.html',
    styleUrls: ['home.component.css']
})
export class HomeComponent implements OnInit {
    user;
    moviesList;
    searchText: string;
    filtersBox: Array<String> = ['None', 'Date', 'Type', 'Langage'];
    selectedFilter: String = 'None';

    constructor(
        private accountService: AccountService,
        private alertService: AlertService
        ) {
        this.user = this.accountService.userValue;
    }

    ngOnInit() {
        console.log('USER ENREGISTRER', this.user.type);
        this.accountService.getMovieByType(this.user.type)
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