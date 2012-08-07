# revision 26777
# category Package
# catalog-ctan /language/japanese/jfontmaps
# catalog-date 2012-04-27 17:19:37 +0200
# catalog-license gpl3
# catalog-version undef
Name:		texlive-jfontmaps
Version:	20120427
Release:	1
Summary:	Font maps for Japanese fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/jfontmaps
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jfontmaps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jfontmaps.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jfontmaps.x86_64-linux.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-jfontmaps.bin = %{EVRD}

%description
The package offers font maps, and supporting material, that
make various Japanese fonts available to users of (u)ptex and
related programs or formats.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/updmap-setup-kanji
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-up-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-up-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-up-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-up-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/otf-up-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-hiragino-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-kozuka-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-morisawa-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/ptex-morisawa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-hiragino-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-hiragino.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-ipa.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-ipaex.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-kozuka-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-kozuka.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-morisawa-04.map
%{_texmfdistdir}/fonts/map/dvipdfmx/jfontmaps/uptex-morisawa.map
%{_texmfdistdir}/scripts/jfontmaps/updmap-setup-kanji.pl
%doc %{_texmfdistdir}/doc/fonts/jfontmaps/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/jfontmaps/README
%doc %{_texmfdistdir}/doc/fonts/jfontmaps/updmap-otf.sh

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/jfontmaps/updmap-setup-kanji.pl updmap-setup-kanji
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
