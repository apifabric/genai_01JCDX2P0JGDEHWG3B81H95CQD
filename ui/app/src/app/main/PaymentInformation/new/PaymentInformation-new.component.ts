import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'PaymentInformation-new',
  templateUrl: './PaymentInformation-new.component.html',
  styleUrls: ['./PaymentInformation-new.component.scss']
})
export class PaymentInformationNewComponent {
  @ViewChild("PaymentInformationForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}