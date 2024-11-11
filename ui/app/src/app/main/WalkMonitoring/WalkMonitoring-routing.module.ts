import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkMonitoringHomeComponent } from './home/WalkMonitoring-home.component';
import { WalkMonitoringNewComponent } from './new/WalkMonitoring-new.component';
import { WalkMonitoringDetailComponent } from './detail/WalkMonitoring-detail.component';

const routes: Routes = [
  {path: '', component: WalkMonitoringHomeComponent},
  { path: 'new', component: WalkMonitoringNewComponent },
  { path: ':id', component: WalkMonitoringDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WalkMonitoring-detail-permissions'
      }
    }
  }
];

export const WALKMONITORING_MODULE_DECLARATIONS = [
    WalkMonitoringHomeComponent,
    WalkMonitoringNewComponent,
    WalkMonitoringDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkMonitoringRoutingModule { }