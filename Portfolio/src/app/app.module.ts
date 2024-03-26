import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BarraNavegacionComponent } from './barra-navegacion/barra-navegacion.component';
import { QuiensoyComponent } from './quiensoy/quiensoy.component';
import { ExperienciaComponent } from './experiencia/experiencia.component';
import { CuriosidadesComponent } from './curiosidades/curiosidades.component';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    BarraNavegacionComponent,
    QuiensoyComponent,
    ExperienciaComponent,
    CuriosidadesComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
