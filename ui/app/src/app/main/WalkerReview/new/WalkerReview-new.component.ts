import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'WalkerReview-new',
  templateUrl: './WalkerReview-new.component.html',
  styleUrls: ['./WalkerReview-new.component.scss']
})
export class WalkerReviewNewComponent {
  @ViewChild("WalkerReviewForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}