import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpParams } from '@angular/common/http';
import { BehaviorSubject, Observable, throwError } from 'rxjs';
import { map } from 'rxjs/operators';

import { environment } from '@environments/environment';
import { User } from '@app/models';

@Injectable({ providedIn: 'root' })
export class AccountService {
    private userSubject: BehaviorSubject<any>;
    public user: Observable<any>;

    constructor(
        private router: Router,
        private http: HttpClient
    ) {
        this.userSubject = new BehaviorSubject(JSON.parse(localStorage.getItem('user')));
        this.user = this.userSubject.asObservable();
    }

    public get userValue() {
        return this.userSubject.value;
    }

    login(email, password) {
        const header = {
            header: "Access-Control-Allow-Headers",
            params: {
                email: email,
                password: password
            }
        };
        const body = {
            email: email,
            password: password
        };
        return this.http.post<any>(`${environment.apiUrl}/login`, body, header)
        .pipe(map(user => {
            if (user["error"]) {
                throw user["error"];
            } else {
                localStorage.setItem('user', JSON.stringify(user));
                console.log(user);
                this.userSubject.next(user);
                return user;
            }
        }));
    }

    logout() {
        const header = {
            header: "Access-Control-Allow-Headers",
            params: { }
        };
        // remove user from local storage and set current user to null
        this.http.post<any>(`${environment.apiUrl}/logout`, { }, header);
        localStorage.removeItem('user');
        this.userSubject.next(null);
        this.router.navigate(['/account/login']);
    }

    register(user: User) {
        const header = {
            header: "Access-Control-Allow-Headers",
            params: {
                email: user.email,
                password: user.password
            }
        };
        const body = {
            email: user.email,
            password: user.password
        };
        console.log("Register ", user);
        return this.http.post(`${environment.apiUrl}/register`, body, header)
        .pipe(map(res => {
            if (res["error"]) {
                throw res["error"];
            } else {
                return res;
            }
        }));
    }

    updateUserType(type) {
        const header = {
            header: "Access-Control-Allow-Headers",
            params: {
                userId: this.userValue.id,
                genre: type
            }
        };
        const body = {
            userId: this.userValue,
            genre: type
        };
        console.log("updateUserType ", type);
        return this.http.post(`${environment.apiUrl}/updateGenre`, body, header)
        .pipe(map(res => {
            if (res["error"]) {
                throw res["error"];
            } else {
                return res;
            }
        }));
    }

    getMovieByType(type) {
        const header = {
            header: "Access-Control-Allow-Headers",
            params: {
                genre: type
            }
        };
        console.log("getMovieByType ", type);
        return this.http.get<any>(`${environment.apiUrl}/getMoviesByGenre`, header)
        .pipe(map(res => {
            if (res["error"]) {
                throw res["error"];
            } else {
                return res.result;
            }
        }));
    }

    getLikedMovies(userId) {
        const header = {
            header: "Access-Control-Allow-Headers",
            params: {
                userId: userId
            }
        };
        console.log("getLikedMovies ", userId);
        return this.http.get<any>(`${environment.apiUrl}/getMovieLiked`, header)
        .pipe(map(res => {
            if (res["error"]) {
                throw res["error"];
            } else {
                return res.result;
            }
        }));
    }

    getWatchedMovies(userId) {
        const header = {
            header: "Access-Control-Allow-Headers",
            params: {
                userId: userId
            }
        };
        console.log("getWatchedMovies ", userId);
        return this.http.get<any>(`${environment.apiUrl}/getMovieSeen`, header)
        .pipe(map(res => {
            if (res["error"]) {
                throw res["error"];
            } else {
                return res.result;
            }
        }));
    }

    getPlaylistsUser(userId) {
        const header = {
            header: "Access-Control-Allow-Headers",
            params: {
                userId: userId
            }
        };
        console.log("getWatchedMovies ", userId);
        return this.http.get<any>(`${environment.apiUrl}/getMovieSeen`, header)
        .pipe(map(res => {
            if (res["error"]) {
                throw res["error"];
            } else {
                return res.result;
            }
        }));
    }
}