#
# Conditional build:
%bcond_without	steam		# without steam hlds engine (use plain hlds)
#
Summary:	Day Of Defeat - linux server
Summary(pl):	Day Of Defeat - serwer dla linuxa
Name:		dod
Version:	v10b
Release:	0.1
License:	Unknown (Distributable)
Group:		Applications/Games
Source0:	%{name}_v10_linux.tar.gz
# Source0-md5:	f438bc12bb9a64c92f8545e9b2d6399c
Source1:	%{name}_%{version}.tar.gz
# Source1-md5:	f5be030178e15bfddd24d1bcf391a22a
URL:		http://www.dayofdefeat.com/
%if %{without steam} Requires:	hlds
%else Requires: hlds-steam
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chroot_home	/home/hlds

%description
Day Of Defeat server for linux

%description -l pl
Serwer dla Day of Defeat

%prep
%setup -q -n dod

%build
cp %{SOURCE1} .
tar zxf %{SOURCE1}
mv -f dod/dlls/* ./dlls/
mv -f dod/readme.txt .
rm -Rf dod
rm -f dod_v10b.tar.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chroot_home}/dod

# todo: mv .so to _libdir
#install -d $RPM_BUILD_ROOT%{_libdir}

# mv is for save space on HDD
mv * $RPM_BUILD_ROOT%{_chroot_home}/dod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc $RPM_BUILD_ROOT%{_chroot_home}/dod/readme.txt $RPM_BUILD_ROOT%{_chroot_home}/dod/manual/*
%dir %{_chroot_home}/dod
%{_chroot_home}/dod/*
