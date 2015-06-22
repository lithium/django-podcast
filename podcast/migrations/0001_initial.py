# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(blank=True, help_text=b'Please choose a child category that corresponds to its respective parent category (e.g., "Design" is a child category of "Arts").<br />If no such child category exists for a parent category (e.g., Comedy, Kids & Family, Music, News & Politics, or TV & Film), simply leave this blank and save.', max_length=50, choices=[(b'Arts', ((b'Design', b'Design'), (b'Fashion & Beauty', b'Fashion & Beauty'), (b'Food', b'Food'), (b'Literature', b'Literature'), (b'Performing Arts', b'Performing Arts'), (b'Visual Arts', b'Visual Arts'))), (b'Business', ((b'Business News', b'Business News'), (b'Careers', b'Careers'), (b'Investing', b'Investing'), (b'Management & Marketing', b'Management & Marketing'), (b'Shopping', b'Shopping'))), (b'Education', ((b'Education Technology', b'Education Technology'), (b'Higher Education', b'Higher Education'), (b'K-12', b'K-12'), (b'Language Courses', b'Language Courses'), (b'Training', b'Training'))), (b'Games & Hobbies', ((b'Automotive', b'Automotive'), (b'Aviation', b'Aviation'), (b'Hobbies', b'Hobbies'), (b'Other Games', b'Other Games'), (b'Video Games', b'Video Games'))), (b'Government & Organizations', ((b'Local', b'Local'), (b'National', b'National'), (b'Non-Profit', b'Non-Profit'), (b'Regional', b'Regional'))), (b'Health', ((b'Alternative Health', b'Alternative Health'), (b'Fitness & Nutrition', b'Fitness & Nutrition'), (b'Self-Help', b'Self-Help'), (b'Sexuality', b'Sexuality'))), (b'Religion & Spirituality', ((b'Buddhism', b'Buddhism'), (b'Christianity', b'Christianity'), (b'Hinduism', b'Hinduism'), (b'Islam', b'Islam'), (b'Judaism', b'Judaism'), (b'Other', b'Other'), (b'Spirituality', b'Spirituality'))), (b'Science & Medicine', ((b'Medicine', b'Medicine'), (b'Natural Sciences', b'Natural Sciences'), (b'Social Sciences', b'Social Sciences'))), (b'Society & Culture', ((b'History', b'History'), (b'Personal Journals', b'Personal Journals'), (b'Philosophy', b'Philosophy'), (b'Places & Travel', b'Places & Travel'))), (b'Sports & Recreation', ((b'Amateur', b'Amateur'), (b'College & High School', b'College & High School'), (b'Outdoor', b'Outdoor'), (b'Professional', b'Professional'))), (b'Technology', ((b'Gadgets', b'Gadgets'), (b'Tech News', b'Tech News'), (b'Podcasting', b'Podcasting'), (b'Software How-To', b'Software How-To')))])),
                ('slug', models.SlugField(help_text=b'A <a href="http://docs.djangoproject.com/en/dev/ref/models/fields/#slugfield">slug</a> is a URL-friendly nickname. For exmaple, a slug for "Fashion & Beauty" is "fashion-beauty".', blank=True)),
            ],
            options={
                'ordering': ['parent', 'slug'],
                'verbose_name': 'category (iTunes child)',
                'verbose_name_plural': 'categories (iTunes child)',
            },
        ),
        migrations.CreateModel(
            name='Enclosure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Title is generally only useful with multiple enclosures.', max_length=255, blank=True)),
                ('file', models.FileField(help_text=b'Either upload or use the "Player" text box below. If uploading, file must be less than or equal to 30 MB for a Google video sitemap.', storage=django.core.files.storage.FileSystemStorage, null=True, upload_to=b'podcasts/episodes/files/', blank=True)),
                ('mime', models.CharField(default=b'video/mp4', max_length=255, verbose_name=b'Format', blank=True, choices=[(b'audio/mpeg', b'.mp3 (audio)'), (b'audio/x-m4a', b'.m4a (audio)'), (b'video/mp4', b'.mp4 (audio or video)'), (b'video/x-m4v', b'.m4v (video)'), (b'video/quicktime', b'.mov (video)'), (b'application/pdf', b'.pdf (document)'), (b'image/jpeg', b'.jpg, .jpeg, .jpe (image)')])),
                ('medium', models.CharField(blank=True, max_length=255, choices=[(b'Audio', b'Audio'), (b'Video', b'Video'), (b'Document', b'Document'), (b'Image', b'Image'), (b'Executable', b'Executable')])),
                ('expression', models.CharField(default=b'Full', max_length=25, blank=True, choices=[(b'Sample', b'Sample'), (b'Full', b'Full'), (b'Nonstop', b'Non-stop')])),
                ('frame', models.CharField(help_text=b'Measured in frames per second (fps), often 29.97.', max_length=5, verbose_name=b'Frame rate', blank=True)),
                ('bitrate', models.CharField(help_text=b'Measured in kilobits per second (kbps), often 128 or 192.', max_length=5, verbose_name=b'Bit rate', blank=True)),
                ('sample', models.CharField(help_text=b'Measured in kilohertz (kHz), often 44.1.', max_length=5, verbose_name=b'Sample rate', blank=True)),
                ('channel', models.CharField(help_text=b'Number of channels; 2 for stereo, 1 for mono.', max_length=5, blank=True)),
                ('algo', models.CharField(blank=True, max_length=50, verbose_name=b'Hash algorithm', choices=[(b'MD5', b'MD5'), (b'SHA-1', b'SHA-1')])),
                ('hash', models.CharField(help_text=b'MD-5 or SHA-1 file hash.', max_length=255, blank=True)),
                ('player', models.URLField(help_text=b'URL of the player console that plays the media. Could be your own .swf, but most likely a YouTube URL, such as <a href="http://www.youtube.com/v/UZCfK8pVztw">http://www.youtube.com/v/UZCfK8pVztw</a> (not the permalink, which looks like <a href="http://www.youtube.com/watch?v=UZCfK8pVztw">http://www.youtube.com/watch?v=UZCfK8pVztw</a>).', blank=True)),
                ('embed', models.BooleanField(help_text=b'Check to allow Google to embed your external player in search results on <a href="http://video.google.com">Google Video</a>.')),
                ('width', models.PositiveIntegerField(help_text=b"Width of the browser window in <br />which the URL should be opened. <br />YouTube's default is 425.", null=True, blank=True)),
                ('height', models.PositiveIntegerField(help_text=b"Height of the browser window in <br />which the URL should be opened. <br />YouTube's default is 344.", null=True, blank=True)),
            ],
            options={
                'ordering': ['mime', 'file'],
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_type', models.CharField(default=b'Plain', max_length=255, verbose_name=b'Title type', blank=True, choices=[(b'Plain', b'Plain text'), (b'HTML', b'HTML')])),
                ('title', models.CharField(help_text=b'Make it specific but avoid explicit language. Limit to 100 characters for a Google video sitemap.', max_length=255)),
                ('slug', models.SlugField(help_text=b'Auto-generated from Title.', unique=True)),
                ('description_type', models.CharField(default=b'Plain', max_length=255, verbose_name=b'Description type', blank=True, choices=[(b'Plain', b'Plain text'), (b'HTML', b'HTML')])),
                ('description', models.TextField(help_text=b'Avoid explicit language. Google video sitempas allow 2,048 characters.')),
                ('captions', models.FileField(help_text=b'For video podcasts. Good captioning choices include <a href="http://en.wikipedia.org/wiki/SubViewer">SubViewer</a>, <a href="http://en.wikipedia.org/wiki/SubRip">SubRip</a> or <a href="http://www.w3.org/TR/ttaf1-dfxp/">TimedText</a>.', storage=django.core.files.storage.FileSystemStorage, upload_to=b'podcasts/episodes/captions/', blank=True)),
                ('category', models.CharField(help_text=b'Limited to one user-specified category for the sake of sanity.', max_length=255, blank=True)),
                ('domain', models.URLField(help_text=b'A URL that identifies a categorization taxonomy.', blank=True)),
                ('frequency', models.CharField(default=b'never', help_text=b"The frequency with which the episode's data changes. For sitemaps.", max_length=10, blank=True, choices=[(b'always', b'Always'), (b'hourly', b'Hourly'), (b'daily', b'Daily'), (b'weekly', b'Weekly'), (b'monthly', b'Monthly'), (b'yearly', b'Yearly'), (b'never', b'Never')])),
                ('priority', models.DecimalField(decimal_places=1, default=b'0.5', max_digits=2, blank=True, help_text=b'The relative priority of this episode compared to others. 1.0 is the most important. For sitemaps.', null=True)),
                ('status', models.IntegerField(default=2, choices=[(1, b'Draft'), (2, b'Public'), (3, b'Private')])),
                ('date', models.DateTimeField(help_text=b'The date/time this episiode is scheduled to go live.')),
                ('update', models.DateTimeField(auto_now=True)),
                ('subtitle', models.CharField(help_text=b'Looks best if only a few words like a tagline.', max_length=255, blank=True)),
                ('summary', models.TextField(help_text=b'Allows 4,000 characters. Description will be used if summary is blank.', blank=True)),
                ('minutes', models.PositiveIntegerField(null=True, blank=True)),
                ('seconds', models.CharField(blank=True, max_length=2, null=True, choices=[(b'00', b'0'), (b'01', b'1'), (b'02', b'2'), (b'03', b'3'), (b'04', b'4'), (b'05', b'5'), (b'06', b'6'), (b'07', b'7'), (b'08', b'8'), (b'09', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31'), (b'32', b'32'), (b'33', b'33'), (b'34', b'34'), (b'35', b'35'), (b'36', b'36'), (b'37', b'37'), (b'38', b'38'), (b'39', b'39'), (b'40', b'40'), (b'41', b'41'), (b'42', b'42'), (b'43', b'43'), (b'44', b'44'), (b'45', b'45'), (b'46', b'46'), (b'47', b'47'), (b'48', b'48'), (b'49', b'49'), (b'50', b'50'), (b'51', b'51'), (b'52', b'52'), (b'53', b'53'), (b'54', b'54'), (b'55', b'55'), (b'56', b'56'), (b'57', b'57'), (b'58', b'58'), (b'59', b'59')])),
                ('keywords', models.CharField(help_text=b'A comma-delimited list of words for searches, up to 12; perhaps include misspellings.', max_length=255, null=True, blank=True)),
                ('explicit', models.CharField(default=b'No', help_text=b'"Clean" will put the clean iTunes graphic by it.', max_length=255, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Clean', b'Clean')])),
                ('block', models.BooleanField(default=False, help_text=b'Check to block this episode from iTunes because <br />its content might cause the entire show to be <br />removed from iTunes.')),
                ('role', models.CharField(blank=True, help_text=b'Role codes provided by the <a href="http://www.ebu.ch/en/technical/metadata/specifications/role_codes.php">European Broadcasting Union</a>.', max_length=255, choices=[(b'Actor', b'Actor'), (b'Adaptor', b'Adaptor'), (b'Anchor person', b'Anchor person'), (b'Animal Trainer', b'Animal Trainer'), (b'Animator', b'Animator'), (b'Announcer', b'Announcer'), (b'Armourer', b'Armourer'), (b'Art Director', b'Art Director'), (b'Artist/Performer', b'Artist/Performer'), (b'Assistant Camera', b'Assistant Camera'), (b'Assistant Chief Lighting Technician', b'Assistant Chief Lighting Technician'), (b'Assistant Director', b'Assistant Director'), (b'Assistant Producer', b'Assistant Producer'), (b'Assistant Visual Editor', b'Assistant Visual Editor'), (b'Author', b'Author'), (b'Broadcast Assistant', b'Broadcast Assistant'), (b'Broadcast Journalist', b'Broadcast Journalist'), (b'Camera Operator', b'Camera Operator'), (b'Carpenter', b'Carpenter'), (b'Casting', b'Casting'), (b'Causeur', b'Causeur'), (b'Chief Lighting Technician', b'Chief Lighting Technician'), (b'Choir', b'Choir'), (b'Choreographer', b'Choreographer'), (b'Clapper Loader', b'Clapper Loader'), (b'Commentary or Commentator', b'Commentary or Commentator'), (b'Commissioning Broadcaster', b'Commissioning Broadcaster'), (b'Composer', b'Composer'), (b'Computer programmer', b'Computer programmer'), (b'Conductor', b'Conductor'), (b'Consultant', b'Consultant'), (b'Continuity Checker', b'Continuity Checker'), (b'Correspondent', b'Correspondent'), (b'Costume Designer', b'Costume Designer'), (b'Dancer', b'Dancer'), (b'Dialogue Coach', b'Dialogue Coach'), (b'Director', b'Director'), (b'Director of Photography', b'Director of Photography'), (b'Distribution Company', b'Distribution Company'), (b'Draughtsman', b'Draughtsman'), (b'Dresser', b'Dresser'), (b'Dubber', b'Dubber'), (b'Editor/Producer (News)', b'Editor/Producer (News)'), (b'Editor-in-chief', b'Editor-in-chief'), (b'Editor-of-the-Day', b'Editor-of-the-Day'), (b'Ensemble', b'Ensemble'), (b'Executive Producer', b'Executive Producer'), (b'Expert', b'Expert'), (b'Fight Director', b'Floor Manager'), (b'Floor Manager', b'Floor Manager'), (b'Focus Puller', b'Focus Puller'), (b'Foley Artist', b'Foley Artist'), (b'Foley Editor', b'Foley Editor'), (b'Foley Mixer', b'Foley Mixer'), (b'Graphic Assistant', b'Graphic Assistant'), (b'Graphic Designer', b'Graphic Designer'), (b'Greensman', b'Greensman'), (b'Grip', b'Grip'), (b'Hairdresser', b'Hairdresser'), (b'Illustrator', b'Illustrator'), (b'Interviewed Guest', b'Interviewed Guest'), (b'Interviewer', b'Interviewer'), (b'Key Character', b'Key Character'), (b'Key Grip', b'Key Grip'), (b'Key Talents', b'Key Talents'), (b'Leadman', b'Leadman'), (b'Librettist', b'Librettist'), (b'Lighting director', b'Lighting director'), (b'Lighting Technician', b'Lighting Technician'), (b'Location Manager', b'Location Manager'), (b'Lyricist', b'Lyricist'), (b'Make Up Artist', b'Make Up Artist'), (b'Manufacturer', b'Manufacturer'), (b'Matte Artist', b'Matte Artist'), (b'Music Arranger', b'Music Arranger'), (b'Music Group', b'Music Group'), (b'Musician', b'Musician'), (b'News Reader', b'News Reader'), (b'Orchestra', b'Orchestra'), (b'Participant', b'Participant'), (b'Photographer', b'Photographer'), (b'Post-Production Editor', b'Post-Production Editor'), (b'Producer', b'Producer'), (b'Production Assistant', b'Production Assistant'), (b'Production Company', b'Production Company'), (b'Production Department', b'Production Department'), (b'Production Manager', b'Production Manager'), (b'Production Secretary', b'Production Secretary'), (b'Programme Production Researcher', b'Programme Production Researcher'), (b'Property Manager', b'Property Manager'), (b'Publishing Company', b'Publishing Company'), (b'Puppeteer', b'Puppeteer'), (b'Pyrotechnician', b'Pyrotechnician'), (b'Reporter', b'Reporter'), (b'Rigger', b'Rigger'), (b'Runner', b'Runner'), (b'Scenario', b'Scenario'), (b'Scenic Operative', b'Scenic Operative'), (b'Script Supervisor', b'Script Supervisor'), (b'Second Assistant Camera', b'Second Assistant Camera'), (b'Second Assistant Director', b'Second Assistant Director'), (b'Second Unit Director', b'Second Unit Director'), (b'Set Designer', b'Set Designer'), (b'Set Dresser', b'Set Dresser'), (b'Sign Language', b'Sign Language'), (b'Singer', b'Singer'), (b'Sound Designer', b'Sound Designer'), (b'Sound Mixer', b'Sound Mixer'), (b'Sound Recordist', b'Sound Recordist'), (b'Special Effects', b'Special Effects'), (b'Stunts', b'Stunts'), (b'Subtitles', b'Subtitles'), (b'Technical Director', b'Technical Director'), (b'Translation', b'Translation'), (b'Transportation Manager', b'Transportation Manager'), (b'Treatment / Programme Proposal', b'Treatment / Programme Proposal'), (b'Vision Mixer', b'Vision Mixer'), (b'Visual Editor', b'Visual Editor'), (b'Visual Effects', b'Visual Effects'), (b'Wardrobe', b'Wardrobe'), (b'Witness', b'Witness')])),
                ('standard', models.CharField(default=b'Simple', max_length=255, blank=True, choices=[(b'Simple', b'Simple'), (b'MPAA', b'MPAA'), (b'V-chip', b'TV Parental Guidelines')])),
                ('rating', models.CharField(default=b'Nonadult', help_text=b'If used, selection must match respective Scheme selection.', max_length=255, blank=True, choices=[(b'Simple', ((b'Adult', b'Adult'), (b'Nonadult', b'Non-adult'))), (b'MPAA', ((b'G', b'G: General Audiences'), (b'PG', b'PG: Parental Guidance Suggested'), (b'PG-13', b'PG-13: Parents Strongly Cautioned'), (b'R', b'R: Restricted'), (b'NC-17', b'NC-17: No One 17 and Under Admitted'))), (b'TV Parental Guidelines', ((b'TV-Y', b'TV-Y: All children'), (b'TV-Y7-FV', b'TV-Y7/TV-Y7-FV: Directed to older children'), (b'TV-G', b'TV-G: General audience'), (b'TV-PG', b'TV-PG: Parental guidance'), (b'TV-14', b'TV-14: Parents strongly cautioned'), (b'TV-MA', b'TV-MA: Mature audiences')))])),
                ('image', models.ImageField(help_text=b'A still image from a video file, but for episode artwork to display in iTunes, image must be <a href="http://answers.yahoo.com/question/index?qid=20080501164348AAjvBvQ">saved to file\'s <strong>metadata</strong></a> before episode uploading!', storage=django.core.files.storage.FileSystemStorage, upload_to=b'podcasts/episodes/img/', blank=True)),
                ('text', models.TextField(help_text=b'Media RSS text transcript. Must use <media:text> tags. Please see the <a href="https://www.google.com/webmasters/tools/video/en/video.html#tagMediaText">Media RSS 2.0</a> specification for syntax.', blank=True)),
                ('deny', models.BooleanField(default=False, help_text=b'Check to deny episode to be shown to users from specified countries.')),
                ('restriction', models.CharField(help_text=b'A space-delimited list of <a href="http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements">ISO 3166-1-coded countries</a>.', max_length=255, blank=True)),
                ('start', models.DateTimeField(help_text=b'Start date and time that the media is valid.', null=True, blank=True)),
                ('end', models.DateTimeField(help_text=b'End date and time that the media is valid.', null=True, blank=True)),
                ('scheme', models.CharField(default=b'W3C-DTF', max_length=255, blank=True)),
                ('name', models.CharField(help_text=b'Any helper name to distinguish this time period.', max_length=255, blank=True)),
                ('preview', models.BooleanField(default=False, help_text=b'Check to allow Google to show a preview of your media in search results.')),
                ('preview_start_mins', models.PositiveIntegerField(help_text=b"Start time (minutes) of the media's preview, <br />shown on Google.com search results before <br />clicking through to see full video.", null=True, verbose_name=b'Preview start (minutes)', blank=True)),
                ('preview_start_secs', models.CharField(choices=[(b'00', b'0'), (b'01', b'1'), (b'02', b'2'), (b'03', b'3'), (b'04', b'4'), (b'05', b'5'), (b'06', b'6'), (b'07', b'7'), (b'08', b'8'), (b'09', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31'), (b'32', b'32'), (b'33', b'33'), (b'34', b'34'), (b'35', b'35'), (b'36', b'36'), (b'37', b'37'), (b'38', b'38'), (b'39', b'39'), (b'40', b'40'), (b'41', b'41'), (b'42', b'42'), (b'43', b'43'), (b'44', b'44'), (b'45', b'45'), (b'46', b'46'), (b'47', b'47'), (b'48', b'48'), (b'49', b'49'), (b'50', b'50'), (b'51', b'51'), (b'52', b'52'), (b'53', b'53'), (b'54', b'54'), (b'55', b'55'), (b'56', b'56'), (b'57', b'57'), (b'58', b'58'), (b'59', b'59')], max_length=2, blank=True, help_text=b"Start time (seconds) of the media's preview.", null=True, verbose_name=b'Preview start (seconds)')),
                ('preview_end_mins', models.PositiveIntegerField(help_text=b"End time (minutes) of the media's preview, <br />shown on Google.com search results before <br />clicking through to see full video.", null=True, verbose_name=b'Preview end (minutes)', blank=True)),
                ('preview_end_secs', models.CharField(choices=[(b'00', b'0'), (b'01', b'1'), (b'02', b'2'), (b'03', b'3'), (b'04', b'4'), (b'05', b'5'), (b'06', b'6'), (b'07', b'7'), (b'08', b'8'), (b'09', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31'), (b'32', b'32'), (b'33', b'33'), (b'34', b'34'), (b'35', b'35'), (b'36', b'36'), (b'37', b'37'), (b'38', b'38'), (b'39', b'39'), (b'40', b'40'), (b'41', b'41'), (b'42', b'42'), (b'43', b'43'), (b'44', b'44'), (b'45', b'45'), (b'46', b'46'), (b'47', b'47'), (b'48', b'48'), (b'49', b'49'), (b'50', b'50'), (b'51', b'51'), (b'52', b'52'), (b'53', b'53'), (b'54', b'54'), (b'55', b'55'), (b'56', b'56'), (b'57', b'57'), (b'58', b'58'), (b'59', b'59')], max_length=2, blank=True, help_text=b"End time (seconds) of the media's preview.", null=True, verbose_name=b'Preview end (seconds)')),
                ('host', models.BooleanField(default=False, help_text=b'Check to allow Google to host your media after it expires. Must set expiration date in Dublin Core.')),
                ('author', models.ManyToManyField(help_text=b'Remember to save the user\'s name and e-mail address in the <a href="../../../auth/user/">User application</a>.', related_name='episode_authors', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date', 'slug'],
            },
        ),
        migrations.CreateModel(
            name='MediaCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, choices=[(b'Action & Adventure', b'Action & Adventure'), (b'Ads & Promotional', b'Ads & Promotional'), (b'Anime & Animation', b'Anime & Animation'), (b'Art & Experimental', b'Art & Experimental'), (b'Business', b'Business'), (b'Children & Family', b'Children & Family'), (b'Comedy', b'Comedy'), (b'Dance', b'Dance'), (b'Documentary', b'Documentary'), (b'Drama', b'Drama'), (b'Educational', b'Educational'), (b'Faith & Spirituality', b'Faith & Spirituality'), (b'Health & Fitness', b'Health & Fitness'), (b'Foreign', b'Foreign'), (b'Gaming', b'Gaming'), (b'Gay & Lesbian', b'Gay & Lesbian'), (b'Home Video', b'Home Video'), (b'Horror', b'Horror'), (b'Independent', b'Independent'), (b'Mature & Adult', b'Mature & Adult'), (b'Movie (feature)', b'Movie (feature)'), (b'Movie (short)', b'Movie (short)'), (b'Movie Trailer', b'Movie Trailer'), (b'Music & Musical', b'Music & Musical'), (b'Nature', b'Nature'), (b'News', b'News'), (b'Political', b'Political'), (b'Religious', b'Religious'), (b'Romance', b'Romance'), (b'Independent', b'Independent'), (b'Sci-Fi & Fantasy', b'Sci-Fi & Fantasy'), (b'Science & Technology', b'Science & Technology'), (b'Special Interest', b'Special Interest'), (b'Sports', b'Sports'), (b'Stock Footage', b'Stock Footage'), (b'Thriller', b'Thriller'), (b'Travel', b'Travel'), (b'TV Show', b'TV Show'), (b'Western', b'Western')])),
                ('slug', models.SlugField(help_text=b'A <a href="http://docs.djangoproject.com/en/dev/ref/models/fields/#slugfield">slug</a> is a URL-friendly nickname. For example, a slug for "Games & Hobbies" is "games-hobbies".', blank=True)),
            ],
            options={
                'ordering': ['slug'],
                'verbose_name': 'category (Media RSS)',
                'verbose_name_plural': 'categories (Media RSS)',
            },
        ),
        migrations.CreateModel(
            name='ParentCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'After saving this parent category, please map it to one or more Child Categories below.', max_length=50, choices=[(b'Arts', b'Arts'), (b'Business', b'Business'), (b'Comedy', b'Comedy'), (b'Education', b'Education'), (b'Games & Hobbies', b'Games & Hobbies'), (b'Government & Organizations', b'Government & Organizations'), (b'Health', b'Health'), (b'Kids & Family', b'Kids & Family'), (b'Music', b'Music'), (b'News & Politics', b'News & Politics'), (b'Religion & Spirituality', b'Religion & Spirituality'), (b'Science & Medicine', b'Science & Medicine'), (b'Society & Culture', b'Society & Culture'), (b'Sports & Recreation', b'Sports & Recreation'), (b'Technology', b'Technology'), (b'TV & Film', b'TV & Film')])),
                ('slug', models.SlugField(help_text=b'A <a href="http://docs.djangoproject.com/en/dev/ref/models/fields/#slugfield">slug</a> is a URL-friendly nickname. For example, a slug for "Games & Hobbies" is "games-hobbies".', blank=True)),
            ],
            options={
                'ordering': ['slug'],
                'verbose_name': 'category (iTunes parent)',
                'verbose_name_plural': 'categories (iTunes parent)',
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.CharField(help_text=b'Name of the organization, company or Web site producing the podcast.', max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text=b'Auto-generated from Title.', unique=True)),
                ('link', models.URLField(help_text=b'URL of either the main website or the podcast section of the main website.')),
                ('description', models.TextField(help_text=b'Describe subject matter, media format, episode schedule and other relevant information while incorporating keywords.')),
                ('language', models.CharField(default=b'en-us', help_text=b'Default is American English. See <a href="http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">ISO 639-1</a> and <a href="http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements">ISO 3166-1</a> for more language codes.', max_length=5, blank=True)),
                ('copyright', models.CharField(default=b'All rights reserved', help_text=b'See <a href="http://creativecommons.org/about/license/">Creative Commons licenses</a> for more information.', max_length=255, choices=[(b'All rights reserved', b'All rights reserved'), (b'Creative Commons: Attribution (by)', b'Creative Commons: Attribution (by)'), (b'Creative Commons: Attribution-Share Alike (by-sa)', b'Creative Commons: Attribution-Share Alike (by-sa)'), (b'Creative Commons: Attribution-No Derivatives (by-nd)', b'Creative Commons: Attribution-No Derivatives (by-nd)'), (b'Creative Commons: Attribution-Non-Commercial (by-nc)', b'Creative Commons: Attribution-Non-Commercial (by-nc)'), (b'Creative Commons: Attribution-Non-Commercial-Share Alike (by-nc-sa)', b'Creative Commons: Attribution-Non-Commercial-Share Alike (by-nc-sa)'), (b'Creative Commons: Attribution-Non-Commercial-No Dreivatives (by-nc-nd)', b'Creative Commons: Attribution-Non-Commercial-No Dreivatives (by-nc-nd)'), (b'Public domain', b'Public domain')])),
                ('copyright_url', models.URLField(help_text=b'A URL pointing to additional copyright information. Consider a <a href="http://creativecommons.org/licenses/">Creative Commons license URL</a>.', verbose_name=b'Copyright URL', blank=True)),
                ('category_show', models.CharField(help_text=b'Limited to one user-specified category for the sake of sanity.', max_length=255, verbose_name=b'Category', blank=True)),
                ('domain', models.URLField(help_text=b'A URL that identifies a categorization taxonomy.', blank=True)),
                ('ttl', models.PositiveIntegerField(help_text=b'"Time to Live," the number of minutes a channel can be cached before refreshing.', null=True, verbose_name=b'TTL', blank=True)),
                ('image', models.ImageField(help_text=b'An attractive, original square JPEG (.jpg) or PNG (.png) image of 600x600 pixels. Image will be scaled down to 50x50 pixels at smallest in iTunes.', storage=django.core.files.storage.FileSystemStorage, upload_to=b'podcasts/shows/img/', blank=True)),
                ('feedburner', models.URLField(help_text=b'Fill this out after saving this show and at least one episode. URL should look like "http://feeds.feedburner.com/TitleOfShow". See <a href="https://github.com/jefftriplett/django-podcast">documentation</a> for more.', verbose_name=b'FeedBurner URL', blank=True)),
                ('subtitle', models.CharField(help_text=b'Looks best if only a few words, like a tagline.', max_length=255, blank=True)),
                ('summary', models.TextField(help_text=b'Allows 4,000 characters. Description will be used if summary is blank.', blank=True)),
                ('explicit', models.CharField(default=b'No', help_text=b'"Clean" will put the clean iTunes graphic by it.', max_length=255, blank=True, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Clean', b'Clean')])),
                ('block', models.BooleanField(default=False, help_text=b'Check to block this show from iTunes. <br />Show will remain blocked until unchecked.')),
                ('redirect', models.URLField(help_text=b"The show's new URL feed if changing the URL of the current show feed. Must continue old feed for at least two weeks and write a 301 redirect for old feed.", blank=True)),
                ('keywords', models.CharField(help_text=b'A comma-demlimited list of up to 12 words for iTunes searches. Perhaps include misspellings of the title.', max_length=255, blank=True)),
                ('itunes', models.URLField(help_text=b'Fill this out after saving this show and at least one episode. URL should look like "http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewPodcast?id=000000000". See <a href="https://github.com/jefftriplett/django-podcast">documentation</a> for more.', verbose_name=b'iTunes Store URL', blank=True)),
                ('author', models.ManyToManyField(help_text=b'Remember to save the user\'s name and e-mail address in the <a href="../../../auth/user/">User application</a>.<br />', related_name='show_authors', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(help_text=b'If selecting a category group with no child category (e.g., Comedy, Kids & Family, Music, News & Politics or TV & Film), save that parent category with a blank <a href="../../childcategory/">child category</a>.<br />Selecting multiple category groups makes the podcast more likely to be found by users.<br />', related_name='show_categories', to='podcast.ChildCategory', blank=True)),
                ('webmaster', models.ForeignKey(related_name='webmaster', blank=True, to=settings.AUTH_USER_MODEL, help_text=b'Remember to save the user\'s name and e-mail address in the <a href="../../../auth/user/">User application</a>.', null=True)),
            ],
            options={
                'ordering': ['organization', 'slug'],
            },
        ),
        migrations.AddField(
            model_name='episode',
            name='media_category',
            field=models.ManyToManyField(related_name='episode_categories', to='podcast.MediaCategory', blank=True),
        ),
        migrations.AddField(
            model_name='episode',
            name='show',
            field=models.ForeignKey(to='podcast.Show'),
        ),
        migrations.AddField(
            model_name='enclosure',
            name='episode',
            field=models.ForeignKey(help_text=b'Include any number of media files; for example, perhaps include an iPhone-optimized, AppleTV-optimized and Flash Video set of video files. Note that the iTunes feed only accepts the first file. More uploading is available after clicking "Save and continue editing."', to='podcast.Episode'),
        ),
        migrations.AddField(
            model_name='childcategory',
            name='parent',
            field=models.ForeignKey(related_name='child_category_parents', to='podcast.ParentCategory'),
        ),
    ]
