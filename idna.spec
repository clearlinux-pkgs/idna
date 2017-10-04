#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : idna
Version  : 2.6
Release  : 23
URL      : http://pypi.debian.net/idna/idna-2.6.tar.gz
Source0  : http://pypi.debian.net/idna/idna-2.6.tar.gz
Summary  : Internationalized Domain Names in Applications (IDNA)
Group    : Development/Tools
License  : ICU
Requires: idna-legacypython
Requires: idna-python3
Requires: idna-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=====================================================
        
        Support for the Internationalised Domain Names in Applications

%package legacypython
Summary: legacypython components for the idna package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the idna package.


%package python
Summary: python components for the idna package.
Group: Default
Requires: idna-legacypython
Requires: idna-python3

%description python
python components for the idna package.


%package python3
Summary: python3 components for the idna package.
Group: Default
Requires: python3-core

%description python3
python3 components for the idna package.


%prep
%setup -q -n idna-2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507155162
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1507155162
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
