filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

function filter_list(l) {
    // Return a new array with the strings filtered out
    for (numero in l) {
      numero = l.filter(Number.isInteger);
    }
    return numero
  }
  
  console.log(filter_list)
  