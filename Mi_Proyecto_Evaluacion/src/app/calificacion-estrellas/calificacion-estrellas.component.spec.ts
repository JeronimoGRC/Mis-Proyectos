import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CalificacionEstrellasComponent } from './calificacion-estrellas.component';

describe('CalificacionEstrellasComponent', () => {
  let component: CalificacionEstrellasComponent;
  let fixture: ComponentFixture<CalificacionEstrellasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CalificacionEstrellasComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CalificacionEstrellasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
