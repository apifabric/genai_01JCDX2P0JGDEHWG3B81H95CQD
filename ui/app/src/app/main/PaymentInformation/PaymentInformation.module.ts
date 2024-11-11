import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {PAYMENTINFORMATION_MODULE_DECLARATIONS, PaymentInformationRoutingModule} from  './PaymentInformation-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    PaymentInformationRoutingModule
  ],
  declarations: PAYMENTINFORMATION_MODULE_DECLARATIONS,
  exports: PAYMENTINFORMATION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class PaymentInformationModule { }