function Agregado() {
    Swal.fire({

        icon: 'success',
        title: 'Your work has been saved',
        showConfirmButton: false,
        timer: 1500
      })
    }



function confirmarborrado(plu_codigo){
    Swal.fire({
        title: 'seguro que desea borrar?',
        text: "no podra deshacer la accion",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: 'Si,Borrar',
        cancelButtonColor: 'Cancelar',
        confirmButtonText: 'Aceptar!'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'Borrado!',
            'El producto ha sido borrado',
            'Hecho'
          ).then(function() {
              window.location.href = "/eliminar_producto/"+ plu_codigo +"/";
          })
        }
      })
}

function confirmarpagar(plu_codigo){
  Swal.fire({
      title: 'seguro que desea borrar?',
      text: "no podra deshacer la accion",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: 'Si,Borrar',
      cancelButtonColor: 'Cancelar',
      confirmButtonText: 'Aceptar!'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Borrado!',
          'El producto ha sido borrado',
          'Hecho'
        ).then(function() {
            window.location.href = "/pagar/";
        })
      }
    })
}

function popupusuario(id_usuario){
  Swal.fire({
      title: 'seguro que desea borrar?',
      text: "no podra deshacer la accion",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: 'Si,Borrar',
      cancelButtonColor: 'Cancelar',
      confirmButtonText: 'Aceptar!'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Borrado!',
          'El usuario ha sido borrado',
          'Hecho'
        ).then(function() {
            window.location.href = "/eliminar_usuario/"+ id_usuario +"/";
        })
      }
    })
}

function epc(id){
  Swal.fire({
      title: 'seguro que desea borrar?',
      text: "no podra deshacer la accion",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: 'Si,Borrar',
      cancelButtonColor: 'Cancelar',
      confirmButtonText: 'Aceptar!'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Borrado!',
          'El producto ha sido borrado',
          'Hecho'
        ).then(function() {
            window.location.href = "/eliminar_carrito/"+ id +"/";
        })
      }
    })
}