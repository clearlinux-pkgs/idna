#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : idna
Version  : 3.1
Release  : 68
URL      : https://files.pythonhosted.org/packages/9f/24/1444ee2c9aee531783c031072a273182109c6800320868ab87675d147a05/idna-3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/9f/24/1444ee2c9aee531783c031072a273182109c6800320868ab87675d147a05/idna-3.1.tar.gz
Summary  : Internationalized Domain Names in Applications (IDNA)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: idna-python = %{version}-%{release}
Requires: idna-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=====================================================
        
        Support for the Internationalised Domain Names in Applications

%package python
Summary: python components for the idna package.
Group: Default
Requires: idna-python3 = %{version}-%{release}

%description python
python components for the idna package.


%package python3
Summary: python3 components for the idna package.
Group: Default
Requires: python3-core
Provides: pypi(idna)

%description python3
python3 components for the idna package.


%prep
%setup -q -n idna-3.1
cd %{_builddir}/idna-3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609792755
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
