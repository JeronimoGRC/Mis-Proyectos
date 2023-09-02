import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AreaSeleccionComponent } from './area-seleccion/area-seleccion.component';
import { ImagenPersonajesComponent } from './imagen-personajes/imagen-personajes.component';
import { AtributosLuchadorComponent } from './atributos-luchador/atributos-luchador.component';
import {HttpClientModule} from "@angular/common/http";
import { BienvenidaComponent } from './bienvenida/bienvenida.component';
import {RouterModule} from "@angular/router";
import { AntesLucharComponent } from './antes-luchar/antes-luchar.component';

@NgModule({
  declarations: [
    AppComponent,
    AreaSeleccionComponent,
    ImagenPersonajesComponent,
    AtributosLuchadorComponent,
    BienvenidaComponent,
    AntesLucharComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    RouterModule.forRoot(
      [
        {path: 'bienvenida', component: BienvenidaComponent},
        {path: 'seleccion', component: AreaSeleccionComponent},
        {path: 'antesLuchador/:id', component: AntesLucharComponent},
        {path: '**', component: BienvenidaComponent},
      ]
    )
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
