import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

// used to create fake backend
import { fakeBackendProvider } from './helpers';

import { AppRoutingModule } from './app-routing.module';
import { JwtInterceptor, ErrorInterceptor } from './helpers';
import { AppComponent } from './app.component';
import { AlertComponent } from './components';
import { HomeComponent } from './home';;
import { PresentationComponent } from './presentation/presentation.component'
import { FilterPipe } from './filter.pipe';;
import { LikedMoviesComponent } from './movies/liked-movies/liked-movies.component';
import { WatchedMoviesComponent } from './movies/watched-movies/watched-movies.component';
import { PlaylistComponent } from './movies/playlist/playlist.component';
import { MovieComponent } from './movies/movie/movie.component';
import { YouTubePlayerModule } from '@angular/youtube-player';

@NgModule({
    imports: [
        BrowserModule,
        ReactiveFormsModule,
        FormsModule,
        HttpClientModule,
        AppRoutingModule,
        YouTubePlayerModule
    ],
    declarations: [
        AppComponent,
        AlertComponent,
        HomeComponent,
        FilterPipe,
        PresentationComponent ,
        LikedMoviesComponent ,
        WatchedMoviesComponent ,
        PlaylistComponent ,
        MovieComponent],
    providers: [
        { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
        { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },

        // provider used to create fake backend
        fakeBackendProvider
    ],
    bootstrap: [AppComponent]
})
export class AppModule { };