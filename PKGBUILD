pkgname='rocker_plugins'
pkgver=1.1.0
pkgrel=1
pkgdesc='Plugins for rocker'
arch=('any')

source=()

_name=${pkgname#python-}

makedepends=('python-setuptools')  # unless it only requires distutils

build() {
    cd ..
    python setup.py build
}

package() {
    cd ..
    python setup.py install --root="$pkgdir" --optimize=1
}
