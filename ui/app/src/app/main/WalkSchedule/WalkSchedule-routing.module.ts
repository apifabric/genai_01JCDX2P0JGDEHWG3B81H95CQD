import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkScheduleHomeComponent } from './home/WalkSchedule-home.component';
import { WalkScheduleNewComponent } from './new/WalkSchedule-new.component';
import { WalkScheduleDetailComponent } from './detail/WalkSchedule-detail.component';

const routes: Routes = [
  {path: '', component: WalkScheduleHomeComponent},
  { path: 'new', component: WalkScheduleNewComponent },
  { path: ':id', component: WalkScheduleDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WalkSchedule-detail-permissions'
      }
    }
  },{
    path: ':walk_schedule_id/Payment', loadChildren: () => import('../Payment/Payment.module').then(m => m.PaymentModule),
    data: {
        oPermission: {
            permissionId: 'Payment-detail-permissions'
        }
    }
},{
    path: ':walk_schedule_id/WalkMonitoring', loadChildren: () => import('../WalkMonitoring/WalkMonitoring.module').then(m => m.WalkMonitoringModule),
    data: {
        oPermission: {
            permissionId: 'WalkMonitoring-detail-permissions'
        }
    }
},{
    path: ':walk_schedule_id/WalkerReview', loadChildren: () => import('../WalkerReview/WalkerReview.module').then(m => m.WalkerReviewModule),
    data: {
        oPermission: {
            permissionId: 'WalkerReview-detail-permissions'
        }
    }
}
];

export const WALKSCHEDULE_MODULE_DECLARATIONS = [
    WalkScheduleHomeComponent,
    WalkScheduleNewComponent,
    WalkScheduleDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkScheduleRoutingModule { }