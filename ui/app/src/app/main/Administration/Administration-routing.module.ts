import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdministrationHomeComponent } from './home/Administration-home.component';
import { AdministrationNewComponent } from './new/Administration-new.component';
import { AdministrationDetailComponent } from './detail/Administration-detail.component';

const routes: Routes = [
  {path: '', component: AdministrationHomeComponent},
  { path: 'new', component: AdministrationNewComponent },
  { path: ':id', component: AdministrationDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Administration-detail-permissions'
      }
    }
  }
];

export const ADMINISTRATION_MODULE_DECLARATIONS = [
    AdministrationHomeComponent,
    AdministrationNewComponent,
    AdministrationDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdministrationRoutingModule { }