import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {HttpClientModule} from "@angular/common/http";
import { InicioComponent } from './inicio/inicio.component';
import { AnadirComponent } from './anadir/anadir.component';
import { EditarComponent } from './editar/editar.component';
import {RouterModule} from "@angular/router";
import { TarjetaPeliculaComponent } from './tarjeta-pelicula/tarjeta-pelicula.component';
import { MatIconModule } from '@angular/material/icon';
import { CalificacionEstrellasComponent } from './calificacion-estrellas/calificacion-estrellas.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";

import {ResolvePeliculaService} from "./service/resolve-pelicula.service";
@NgModule({
  declarations: [
    AppComponent,
    InicioComponent,
    AnadirComponent,
    EditarComponent,
    TarjetaPeliculaComponent,
    CalificacionEstrellasComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatIconModule,
    RouterModule.forRoot(
      [
        {path: 'inicio', component: InicioComponent,resolve: {
                                              movies: ResolvePeliculaService
          }},
        {path: 'anadir', component: AnadirComponent},
        {path: 'editar/:id', component: EditarComponent},
        {path: '**', redirectTo: '/inicio', pathMatch: "full"},
        {path: '', redirectTo: '/inicio', pathMatch: "full"},
      ]
    ),
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
