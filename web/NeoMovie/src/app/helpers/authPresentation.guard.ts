import { Injectable } from '@angular/core';
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';

import { AccountService } from '@app/services';

@Injectable({ providedIn: 'root' })
export class AuthGuardPresentation implements CanActivate {
    constructor(
        private router: Router,
        private accountService: AccountService
    ) {}

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        const user = this.accountService.userValue;
        if (user) {
            // not logged in so redirect to presentation page with the return url
            this.router.navigate(['/home'], { queryParams: { returnUrl: state.url }});
            return true;
        }

        // authorised so return true
        return true;
    }
}