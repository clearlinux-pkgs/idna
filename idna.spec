#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : idna
Version  : 2.0
Release  : 6
URL      : https://pypi.python.org/packages/source/i/idna/idna-2.0.tar.gz
Source0  : https://pypi.python.org/packages/source/i/idna/idna-2.0.tar.gz
Summary  : Internationalized Domain Names in Applications (IDNA)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: idna-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Internationalized Domain Names in Applications (IDNA)
=====================================================

%package python
Summary: python components for the idna package.
Group: Default

%description python
python components for the idna package.


%prep
%setup -q -n idna-2.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
python2 setup.py test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
