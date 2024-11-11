import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {WALKMONITORING_MODULE_DECLARATIONS, WalkMonitoringRoutingModule} from  './WalkMonitoring-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    WalkMonitoringRoutingModule
  ],
  declarations: WALKMONITORING_MODULE_DECLARATIONS,
  exports: WALKMONITORING_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WalkMonitoringModule { }