import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AccountService, AlertService } from '@app/services';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-playlist',
  templateUrl: './playlist.component.html',
  styleUrls: ['./playlist.component.less']
})
export class PlaylistComponent implements OnInit {

  user;
  playlists = [];

  constructor(
    private accountService: AccountService,
    private alertService: AlertService,
    private router: Router
    ) {
    this.user = this.accountService.userValue;
}

  ngOnInit(): void {
    this.accountService.getPlaylistsUser(this.user.id)
    .pipe(first())
    .subscribe(
        (playlists) => {
            this.playlists = playlists
            console.log(playlists);
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

}
