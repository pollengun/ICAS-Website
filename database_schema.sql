-- icas_activity
CREATE TABLE "icas_activity" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(300) NOT NULL, "description" text NOT NULL, "image" varchar(100) NULL, "date" date NOT NULL, "order" integer NOT NULL, "related_event_id" bigint NULL REFERENCES "icas_event" ("id") DEFERRABLE INITIALLY DEFERRED, "related_project_id" bigint NULL REFERENCES "icas_project" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_activity_participants
CREATE TABLE "icas_activity_participants" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "activity_id" bigint NOT NULL REFERENCES "icas_activity" ("id") DEFERRABLE INITIALLY DEFERRED, "teammember_id" bigint NOT NULL REFERENCES "icas_teammember" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_contactmessage
CREATE TABLE "icas_contactmessage" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "email" varchar(254) NOT NULL, "subject" varchar(300) NOT NULL, "message" text NOT NULL, "submitted_at" datetime NOT NULL, "is_read" bool NOT NULL, "assigned_to_id" bigint NULL REFERENCES "icas_teammember" ("id") DEFERRABLE INITIALLY DEFERRED, "related_project_id" bigint NULL REFERENCES "icas_project" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_event
CREATE TABLE "icas_event" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(300) NOT NULL, "event_type" varchar(20) NOT NULL, "description" text NOT NULL, "date" date NOT NULL, "time" time NULL, "venue" varchar(300) NOT NULL, "image" varchar(100) NULL, "registration_link" varchar(200) NOT NULL, "is_featured" bool NOT NULL);

-- icas_event_organizers
CREATE TABLE "icas_event_organizers" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "event_id" bigint NOT NULL REFERENCES "icas_event" ("id") DEFERRABLE INITIALLY DEFERRED, "teammember_id" bigint NOT NULL REFERENCES "icas_teammember" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_event_related_projects
CREATE TABLE "icas_event_related_projects" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "event_id" bigint NOT NULL REFERENCES "icas_event" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" bigint NOT NULL REFERENCES "icas_project" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_event_research_areas
CREATE TABLE "icas_event_research_areas" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "event_id" bigint NOT NULL REFERENCES "icas_event" ("id") DEFERRABLE INITIALLY DEFERRED, "researcharea_id" bigint NOT NULL REFERENCES "icas_researcharea" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_news
CREATE TABLE "icas_news" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(300) NOT NULL, "content" text NOT NULL, "date_posted" date NOT NULL, "image" varchar(100) NULL, "is_featured" bool NOT NULL);

-- icas_news_related_events
CREATE TABLE "icas_news_related_events" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "news_id" bigint NOT NULL REFERENCES "icas_news" ("id") DEFERRABLE INITIALLY DEFERRED, "event_id" bigint NOT NULL REFERENCES "icas_event" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_news_related_projects
CREATE TABLE "icas_news_related_projects" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "news_id" bigint NOT NULL REFERENCES "icas_news" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" bigint NOT NULL REFERENCES "icas_project" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_news_related_publications
CREATE TABLE "icas_news_related_publications" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "news_id" bigint NOT NULL REFERENCES "icas_news" ("id") DEFERRABLE INITIALLY DEFERRED, "publication_id" bigint NOT NULL REFERENCES "icas_publication" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_partner
CREATE TABLE "icas_partner" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "logo" varchar(100) NULL, "website" varchar(200) NOT NULL, "order" integer NOT NULL);

-- icas_project
CREATE TABLE "icas_project" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(300) NOT NULL, "description" text NOT NULL, "status" varchar(20) NOT NULL, "start_date" date NOT NULL, "end_date" date NULL, "funding_agency" varchar(200) NOT NULL, "budget" varchar(100) NOT NULL, "image" varchar(100) NULL, "principal_investigator_id" bigint NULL REFERENCES "icas_teammember" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_project_partners
CREATE TABLE "icas_project_partners" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "project_id" bigint NOT NULL REFERENCES "icas_project" ("id") DEFERRABLE INITIALLY DEFERRED, "partner_id" bigint NOT NULL REFERENCES "icas_partner" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_project_research_areas
CREATE TABLE "icas_project_research_areas" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "project_id" bigint NOT NULL REFERENCES "icas_project" ("id") DEFERRABLE INITIALLY DEFERRED, "researcharea_id" bigint NOT NULL REFERENCES "icas_researcharea" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_project_team_members
CREATE TABLE "icas_project_team_members" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "project_id" bigint NOT NULL REFERENCES "icas_project" ("id") DEFERRABLE INITIALLY DEFERRED, "teammember_id" bigint NOT NULL REFERENCES "icas_teammember" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_publication
CREATE TABLE "icas_publication" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(500) NOT NULL, "authors" varchar(500) NOT NULL, "pub_type" varchar(20) NOT NULL, "journal_or_venue" varchar(300) NOT NULL, "year" integer NOT NULL, "doi" varchar(200) NOT NULL, "abstract" text NOT NULL, "pdf_link" varchar(200) NOT NULL);

-- icas_publication_projects
CREATE TABLE "icas_publication_projects" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "publication_id" bigint NOT NULL REFERENCES "icas_publication" ("id") DEFERRABLE INITIALLY DEFERRED, "project_id" bigint NOT NULL REFERENCES "icas_project" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_publication_research_areas
CREATE TABLE "icas_publication_research_areas" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "publication_id" bigint NOT NULL REFERENCES "icas_publication" ("id") DEFERRABLE INITIALLY DEFERRED, "researcharea_id" bigint NOT NULL REFERENCES "icas_researcharea" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_publication_team_members
CREATE TABLE "icas_publication_team_members" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "publication_id" bigint NOT NULL REFERENCES "icas_publication" ("id") DEFERRABLE INITIALLY DEFERRED, "teammember_id" bigint NOT NULL REFERENCES "icas_teammember" ("id") DEFERRABLE INITIALLY DEFERRED);

-- icas_researcharea
CREATE TABLE "icas_researcharea" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "description" text NOT NULL, "icon" varchar(100) NOT NULL, "order" integer NOT NULL);

-- icas_teammember
CREATE TABLE "icas_teammember" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "role" varchar(20) NOT NULL, "designation" varchar(200) NOT NULL, "bio" text NOT NULL, "photo" varchar(100) NULL, "email" varchar(254) NOT NULL, "linkedin" varchar(200) NOT NULL, "google_scholar" varchar(200) NOT NULL, "order" integer NOT NULL, "department" varchar(200) NOT NULL, "phone" varchar(100) NOT NULL, "qualification" varchar(200) NOT NULL, "show_on_contact_page" bool NOT NULL, "university" varchar(200) NOT NULL);

-- icas_teammember_research_areas
CREATE TABLE "icas_teammember_research_areas" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "teammember_id" bigint NOT NULL REFERENCES "icas_teammember" ("id") DEFERRABLE INITIALLY DEFERRED, "researcharea_id" bigint NOT NULL REFERENCES "icas_researcharea" ("id") DEFERRABLE INITIALLY DEFERRED);