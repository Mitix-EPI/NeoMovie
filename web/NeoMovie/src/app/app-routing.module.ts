import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home';
import { AuthGuard } from './helpers';
import { PresentationComponent } from './presentation/presentation.component';
import { AuthGuardPresentation } from './helpers/authPresentation.guard';
import { LikedMoviesComponent } from './movies/liked-movies/liked-movies.component';
import { WatchedMoviesComponent } from './movies/watched-movies/watched-movies.component';
import { PlaylistComponent } from './movies/playlist/playlist.component';
import { MovieComponent } from './movies/movie/movie.component';

const accountModule = () => import('./account/account.module').then(x => x.AccountModule);

const routes: Routes = [
    { path: '', component: PresentationComponent, canActivate: [AuthGuardPresentation] },
    { path: 'home', component: HomeComponent, canActivate: [AuthGuard] },
    { path: 'account', loadChildren: accountModule },
    { path: 'movie/:id', component: MovieComponent, canActivate: [AuthGuard] },
    { path: 'likedMovies', component: LikedMoviesComponent, canActivate: [AuthGuard] },
    { path: 'watchedMovies', component: WatchedMoviesComponent, canActivate: [AuthGuard] },
    { path: 'playlists', component: PlaylistComponent, canActivate: [AuthGuard] },

    // otherwise redirect to home
    { path: '**', redirectTo: '' }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }