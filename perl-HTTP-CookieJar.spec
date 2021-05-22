#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-CookieJar
Version  : 0.010
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/HTTP-CookieJar-0.010.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/HTTP-CookieJar-0.010.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhttp-cookiejar-perl/libhttp-cookiejar-perl_0.008-1.debian.tar.xz
Summary  : 'A minimalist HTTP user agent cookie jar'
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 MIT
Requires: perl-HTTP-CookieJar-license = %{version}-%{release}
Requires: perl-HTTP-CookieJar-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(URI)

%description
NAME
HTTP::CookieJar - A minimalist HTTP user agent cookie jar
VERSION
version 0.010

%package dev
Summary: dev components for the perl-HTTP-CookieJar package.
Group: Development
Provides: perl-HTTP-CookieJar-devel = %{version}-%{release}
Requires: perl-HTTP-CookieJar = %{version}-%{release}

%description dev
dev components for the perl-HTTP-CookieJar package.


%package license
Summary: license components for the perl-HTTP-CookieJar package.
Group: Default

%description license
license components for the perl-HTTP-CookieJar package.


%package perl
Summary: perl components for the perl-HTTP-CookieJar package.
Group: Default
Requires: perl-HTTP-CookieJar = %{version}-%{release}

%description perl
perl components for the perl-HTTP-CookieJar package.


%prep
%setup -q -n HTTP-CookieJar-0.010
cd %{_builddir}
tar xf %{_sourcedir}/libhttp-cookiejar-perl_0.008-1.debian.tar.xz
cd %{_builddir}/HTTP-CookieJar-0.010
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTTP-CookieJar-0.010/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-CookieJar
cp %{_builddir}/HTTP-CookieJar-0.010/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-CookieJar/e188c4892bc1fbfced62c2299a2a24fd21098d81
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTTP-CookieJar/fd6bfa7ce6e209c152c6304916a7bf6f05be81d1
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::CookieJar.3
/usr/share/man/man3/HTTP::CookieJar::LWP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-CookieJar/e188c4892bc1fbfced62c2299a2a24fd21098d81
/usr/share/package-licenses/perl-HTTP-CookieJar/fd6bfa7ce6e209c152c6304916a7bf6f05be81d1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/CookieJar.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/CookieJar/LWP.pm
