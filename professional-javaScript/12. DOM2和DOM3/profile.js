function profile(func, arguments) {
    console.time(func.name)
    func(...arguments)
    console.timeEnd(func.name)
}

function test(n, m) {
    for (var i=0; i<n; i++) {

    }
}

profile(test, [10, 20])

