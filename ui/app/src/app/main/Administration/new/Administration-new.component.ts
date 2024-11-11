import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Administration-new',
  templateUrl: './Administration-new.component.html',
  styleUrls: ['./Administration-new.component.scss']
})
export class AdministrationNewComponent {
  @ViewChild("AdministrationForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}