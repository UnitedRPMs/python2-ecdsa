%global srcname ecdsa

Name:           python2-%{srcname}
Version:        0.13.3
Release:        7%{?dist}
Summary:        ECDSA cryptographic signature library

License:        MIT
URL:            https://pypi.python.org/pypi/ecdsa
Source0:        https://pypi.python.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
# Fedora's openssl does not support 192 and 224 bit keys, so don't test against that
Patch0:         python-ecdsa-noweak.patch

BuildArch:      noarch
# For tests
BuildRequires:  openssl
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-six
BuildRequires:	python2-rpm-macros
Requires:       python2-six
%{?python_provide:%python_provide python2-%{srcname}}

%description 
This is an easy-to-use implementation of ECDSA cryptography (Elliptic Curve
Digital Signature Algorithm), implemented purely in Python, released under
the MIT license. With this library, you can quickly create keypairs (signing
key and verifying key), sign messages, and verify the signatures. The keys
and signatures are very short, making them easy to handle and incorporate
into other protocols.

%prep
%setup -n %{srcname}-%{version} 
%patch0 -p1 -b .noweak
rm -rf %{srcname}.egg-info
# Remove extraneous #!
find ecdsa -name \*.py | xargs sed -ie '/\/usr\/bin\/env/d'
# Use system python-six
find -name \*.py | xargs sed -ie 's/from \(ecdsa\|\)\.six/from six/g'
rm ecdsa/six.py


%build
%py2_build

%install
%py2_install


%check
%{__python2} setup.py test

 
%files 
%license LICENSE
%doc NEWS README.md
%{python2_sitelib}/*

%changelog

* Thu Oct 31 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.13.3-7
- Updated to 0.13.3

* Mon Feb 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.13-18
- Upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13-12
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.13-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Orion Poplawski <orion@nwra.com> - 0.13-9
- Modernize spec

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.13-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 5 2016 Orion Poplawski <orion@cora.nwra.com> - 0.13-4
- Enable python3 builds for EPEL7

* Sat Feb 13 2016 Orion Poplawski <orion@cora.nwra.com> - 0.13-3
- Fix provide typo

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Orion Poplawski <orion@cora.nwra.com> - 0.13-1
- Update to 0.13
- Modernize spec

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.11-2
- Rebuild for Python 3.4

* Sat May 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.11-1
- Update to 0.11

* Mon Feb 24 2014 Orion Poplawski <orion@cora.nwra.com> - 0.10-3
- Add python3 package

* Mon Feb 24 2014 Orion Poplawski <orion@cora.nwra.com> - 0.10-2
- Use system python-six
- Remove extraneous #!s

* Fri Feb 21 2014 Orion Poplawski <orion@cora.nwra.com> - 0.10-1
- Initial package
