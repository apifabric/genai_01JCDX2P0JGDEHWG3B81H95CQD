import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkerHomeComponent } from './home/Walker-home.component';
import { WalkerNewComponent } from './new/Walker-new.component';
import { WalkerDetailComponent } from './detail/Walker-detail.component';

const routes: Routes = [
  {path: '', component: WalkerHomeComponent},
  { path: 'new', component: WalkerNewComponent },
  { path: ':id', component: WalkerDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Walker-detail-permissions'
      }
    }
  },{
    path: ':walker_id/Payment', loadChildren: () => import('../Payment/Payment.module').then(m => m.PaymentModule),
    data: {
        oPermission: {
            permissionId: 'Payment-detail-permissions'
        }
    }
},{
    path: ':walker_id/WalkSchedule', loadChildren: () => import('../WalkSchedule/WalkSchedule.module').then(m => m.WalkScheduleModule),
    data: {
        oPermission: {
            permissionId: 'WalkSchedule-detail-permissions'
        }
    }
},{
    path: ':walker_id/WalkerAvailability', loadChildren: () => import('../WalkerAvailability/WalkerAvailability.module').then(m => m.WalkerAvailabilityModule),
    data: {
        oPermission: {
            permissionId: 'WalkerAvailability-detail-permissions'
        }
    }
},{
    path: ':walker_id/WalkerRate', loadChildren: () => import('../WalkerRate/WalkerRate.module').then(m => m.WalkerRateModule),
    data: {
        oPermission: {
            permissionId: 'WalkerRate-detail-permissions'
        }
    }
}
];

export const WALKER_MODULE_DECLARATIONS = [
    WalkerHomeComponent,
    WalkerNewComponent,
    WalkerDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkerRoutingModule { }