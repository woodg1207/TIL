function doSomethin(subject, callback) {
  console.log(`이제 ${subject} 과목평가 준비를 시작해 볼까?`)
  callback()
}

function alertFinish() {
  console.log('얼마 안남았는데?')
}

doSomethin('django', alertFinish)

