import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-presentation',
  templateUrl: './presentation.component.html',
  styleUrls: ['./presentation.component.less']
})
export class PresentationComponent implements OnInit {

  constructor(
    private router: Router,
  ) { }

  ngOnInit(): void {
  }

  goLogin() {
    this.router.navigateByUrl('/account/login');
  }

  goRegister() {
    this.router.navigateByUrl('/account/register');
  }

}
