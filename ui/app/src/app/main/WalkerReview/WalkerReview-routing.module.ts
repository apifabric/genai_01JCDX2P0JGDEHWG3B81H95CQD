import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WalkerReviewHomeComponent } from './home/WalkerReview-home.component';
import { WalkerReviewNewComponent } from './new/WalkerReview-new.component';
import { WalkerReviewDetailComponent } from './detail/WalkerReview-detail.component';

const routes: Routes = [
  {path: '', component: WalkerReviewHomeComponent},
  { path: 'new', component: WalkerReviewNewComponent },
  { path: ':id', component: WalkerReviewDetailComponent,
    data: {
      oPermission: {
        permissionId: 'WalkerReview-detail-permissions'
      }
    }
  }
];

export const WALKERREVIEW_MODULE_DECLARATIONS = [
    WalkerReviewHomeComponent,
    WalkerReviewNewComponent,
    WalkerReviewDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WalkerReviewRoutingModule { }