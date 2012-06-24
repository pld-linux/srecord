Summary:	Manipulate EPROM load files
Summary(pl):	Operacje na plikach do programowania pami�ci (E)EPROM i Flash
Name:		srecord
Version:	1.23
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://srecord.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	fcca798d3cc3f186410b8ed0e1c2e793
Patch0:		%{name}-man_fastload.patch
URL:		http://srecord.sourceforge.net/
BuildRequires:  bison
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SRecord package is a collection of powerful tools for manipulating
EPROM load files.

- The SRecord package understands a number of file formats: Motorola
  S-Record, Intel, Tektronix, Binary. These file formats may be read and
  written. Also C array definitions, for output only.

- The SRecord package has a number of tools: srec_cat for copying and
  and converting files, srec_cmp for comparing files and srec_info for
  printing summaries.

- The SRecord package has a number for filters: checksum to add
  checksums to the data, crop to keep address ranges, exclude to remove
  address ranges, fill to plug holes in the data, length to insert the
  data length, maximum to insert the data address maximum, minimum to
  insert the data address minimum, offset to adjust addresses, and split
  for wide data buses and memory striping.

More than one filter may be applied to each input file. Different
filters may be applied to each input file. All filters may be applied
to all file formats.

%description -l pl
Pakiet SRecord to zbi�r narz�dzi do modyfikacji plik�w u�ywanych do
programowania pami�ci (E)EPROM i Flash.

- Odczytywane i zapisywane s� pliki w nast�puj�cych formatach:
  Motorola S-Record, Intel, Tektronix, Binary.

- W pakiecie znajduj� si� nast�puj�ce narz�dzia: srec_cat - do
  kopiowania i konwersji plik�w, srec_cmp - do por�wnywania plik�w,
  srec_info - do wy�wietlania informacji o plikach.

- Dost�pne s� nast�puj�ce filtry: cheksum - dodawanie sumy kontrolnej
  do danych, crop - usuwanie danych spoza podanego zakresu adres�w,
  exclude - usuwanie danych z podanego zakresu adres�w, fill -
  wype�nianie podanego zakresu adres�w, length - dodawanie d�ugo�ci
  danych, maximum - dodawanie najwi�kszego adresu z danych wej�ciowych,
  minimum - dodawanie najmniejszego adresu z danych wej�ciowych, offset
  - modyfikowanie adres�w o podan� warto��, split - rozdzielanie danych
  wej�ciowych na podzbiory.

Dla ka�dego pliku wej�ciowego mo�e by� dodanych po kilka filtr�w
wej�ciowych. Ka�dy z filtr�w mo�e by� stosowany do ka�dego z format�w
plik�w.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUILDING README
%attr(755,root,root) %{_bindir}/srec_cat
%attr(755,root,root) %{_bindir}/srec_cmp
%attr(755,root,root) %{_bindir}/srec_info
%{_mandir}/man1/*
%{_mandir}/man5/*
