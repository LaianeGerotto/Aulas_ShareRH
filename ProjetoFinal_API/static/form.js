const alertaDeletar = (event) => {
  if (confirm("Confirma a exclusão do Registro?")){
    event.target.parentElement.submit()
  } else {
    event.stopPropagation()
    event.preventDefault()
  }
}