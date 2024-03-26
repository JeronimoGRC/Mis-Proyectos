import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { QuiensoyComponent } from './quiensoy/quiensoy.component';
import { ExperienciaComponent } from './experiencia/experiencia.component';
import { CuriosidadesComponent } from './curiosidades/curiosidades.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'quiensoy', component: QuiensoyComponent},
  {path: 'experiencia', component: ExperienciaComponent},
  {path: 'curiosidades', component: CuriosidadesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
