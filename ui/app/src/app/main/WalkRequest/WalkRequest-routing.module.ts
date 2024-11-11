import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkRequestHomeComponent } from './home/WalkRequest-home.component';
import { WalkRequestNewComponent } from './new/WalkRequest-new.component';
import { WalkRequestDetailComponent } from './detail/WalkRequest-detail.component';

const routes: Routes = [
  {path: '', component: WalkRequestHomeComponent},
  { path: 'new', component: WalkRequestNewComponent },
  { path: ':id', component: WalkRequestDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WalkRequest-detail-permissions'
      }
    }
  },{
    path: ':walk_request_id/WalkSchedule', loadChildren: () => import('../WalkSchedule/WalkSchedule.module').then(m => m.WalkScheduleModule),
    data: {
        oPermission: {
            permissionId: 'WalkSchedule-detail-permissions'
        }
    }
}
];

export const WALKREQUEST_MODULE_DECLARATIONS = [
    WalkRequestHomeComponent,
    WalkRequestNewComponent,
    WalkRequestDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkRequestRoutingModule { }