import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'WalkMonitoring-new',
  templateUrl: './WalkMonitoring-new.component.html',
  styleUrls: ['./WalkMonitoring-new.component.scss']
})
export class WalkMonitoringNewComponent {
  @ViewChild("WalkMonitoringForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}