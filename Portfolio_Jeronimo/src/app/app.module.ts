import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { QuiensoyComponent } from './quiensoy/quiensoy.component';
import { ExperienciaComponent } from './experiencia/experiencia.component';
import { CuriosidadesComponent } from './curiosidades/curiosidades.component';
import { AppComponent } from './app.component';



@NgModule({
  declarations: [
/*    AppComponent,
    QuiensoyComponent,
    ExperienciaComponent,
    CuriosidadesComponent*/
  ],
  imports: [
    CommonModule,
    RouterModule.forRoot(
      [
        {path: 'quienSoy', component: QuiensoyComponent},
        {path: 'experiencia', component: ExperienciaComponent},
        {path: 'curiosidades', component: CuriosidadesComponent}
      ]
    )
  ],
  exports: [RouterModule]

})
export class AppModule { }
