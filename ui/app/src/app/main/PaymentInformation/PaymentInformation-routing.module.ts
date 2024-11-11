import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PaymentInformationHomeComponent } from './home/PaymentInformation-home.component';
import { PaymentInformationNewComponent } from './new/PaymentInformation-new.component';
import { PaymentInformationDetailComponent } from './detail/PaymentInformation-detail.component';

const routes: Routes = [
  {path: '', component: PaymentInformationHomeComponent},
  { path: 'new', component: PaymentInformationNewComponent },
  { path: ':id', component: PaymentInformationDetailComponent,
    data: {
      oPermission: {
        permissionId: 'PaymentInformation-detail-permissions'
      }
    }
  }
];

export const PAYMENTINFORMATION_MODULE_DECLARATIONS = [
    PaymentInformationHomeComponent,
    PaymentInformationNewComponent,
    PaymentInformationDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PaymentInformationRoutingModule { }