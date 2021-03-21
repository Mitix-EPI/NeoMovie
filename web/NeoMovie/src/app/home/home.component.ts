import { Component, OnInit } from '@angular/core';

import { AccountService } from '@app/services';
import { first } from 'rxjs/operators';
import { AlertService } from '../services/alert.service';
import { Router } from '@angular/router';

@Component({
    templateUrl: 'home.component.html',
    styleUrls: ['home.component.css']
})
export class HomeComponent implements OnInit {
    user;
    moviesList;
    moviesTypeList;
    searchText: string;
    filtersBox: Array<String> = ['None', 'Date', 'Type', 'Langage'];
    selectedFilter: String = 'None';

    constructor(
        private accountService: AccountService,
        private alertService: AlertService,
        private router: Router
        ) {
        this.user = this.accountService.userValue;
    }

    ngOnInit() {
        this.accountService.getAllMovies()
        .pipe(first())
        .subscribe(
            (movies) => {
                console.log("AllMovies", movies);
                this.moviesList = movies
                this.accountService.getMovieByType(this.user.type)
                .pipe(first())
                .subscribe(
                    (movies) => {
                        console.log("Movies by Type", movies);
                        this.moviesTypeList = movies
                        console.log(movies);
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