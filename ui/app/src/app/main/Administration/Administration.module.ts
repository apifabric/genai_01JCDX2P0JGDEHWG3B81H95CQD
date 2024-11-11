import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {ADMINISTRATION_MODULE_DECLARATIONS, AdministrationRoutingModule} from  './Administration-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    AdministrationRoutingModule
  ],
  declarations: ADMINISTRATION_MODULE_DECLARATIONS,
  exports: ADMINISTRATION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AdministrationModule { }