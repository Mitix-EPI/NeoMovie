import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AccountService, AlertService } from '@app/services';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-first-time',
  templateUrl: './first-time.component.html',
})
export class FirstTimeComponent implements OnInit {

  form: FormGroup;
  loading: boolean = false;
  submitted: boolean = false;
  returnUrl: string;
  Types: Array<String> = ['Horror', 'Science Fiction', 'Romance', 'Animation', 'Humor'];

  constructor(
        private formBuilder: FormBuilder,
        private route: ActivatedRoute,
        private router: Router,
        private accountService: AccountService,
        private alertService: AlertService
  ) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      type: ['', Validators.required]
    });

    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/home';
  }

  get f() { return this.form.controls; }

  onSubmit() {
    this.submitted = true;

    // reset alerts on submit
    this.alertService.clear();

    // stop here if form is invalid
    if (this.form.invalid) {
      return;
    }
    this.loading = true;
    this.accountService.updateUserType(this.f.type.value)
    .pipe(first())
    .subscribe(
      data => {
        console.log(data);
        this.router.navigateByUrl('/home');
      },
      error => {
        this.alertService.error(error);
                this.loading = false;
      }
    );
  }

}
