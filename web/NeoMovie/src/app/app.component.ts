import { Component } from '@angular/core';

import { AccountService } from './services';
import { User } from './models';
import { Location } from '@angular/common';

@Component({
    selector: 'app',
    templateUrl: 'app.component.html',
    styleUrls: ['./app.component.scss']
})
export class AppComponent {
    user: User;

    constructor(private accountService: AccountService, public location: Location) {
        this.accountService.user.subscribe(x => this.user = x);
    }

    logout() {
        this.accountService.logout();
    }
}