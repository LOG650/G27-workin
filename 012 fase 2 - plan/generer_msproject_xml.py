"""
Generer MS Project XML for Prognoseprosjekt G27 (LOG650, HiM).

Outputfilen `Prosjektplan_G27_oppdatert.xml` kan importeres direkte i MS Project:
    File -> Open -> velg *.xml (Type: XML Format).

Endringer fra forrige plan (Prosjektplan gant27feb.mpp / PDF datert 02.03.26):
  1. Synkronisert med faktisk fremdrift per 2026-05-29 (status.md).
  2. Lagt til M-05 Peer review gjennomført som egen milepæl.
  3. Lagt til ACT-13 Eksamensforberedelser som egen aktivitet.
  4. Korrigert Fase 4 slutt-dato fra 01.07.26 til 05.06.26.
  5. Slått sammen WBS og Gantt-plan til én ACT-05 (samsvarer med status.md).
  6. Fjernet «Skriving av konklusjon» som lufthengende aktivitet (subsumert i ACT-11).
  7. Eksplisitte FS-/SS-avhengigheter mellom aktiviteter.
  8. ACT-07 Datavask reflekterer faktisk varighet etter RELEX-rework (16.02-15.04).
  9. % fullført oppdatert for alle aktiviteter.
"""
from pathlib import Path

# ----- Prosjektmetadata -----
PROJECT_NAME = "Prognoseprosjekt G27"
PROJECT_TITLE = "Prognoseprosjekt LOG650 G27 – Prosjektplan (oppdatert 29.05.26)"
PROJECT_AUTHOR = "Line Lyngsnes Johansen og Amanda Arnesen Almaas"
PROJECT_MANAGER = "Bård Inge Austigard Pettersen"
PROJECT_COMPANY = "Høgskolen i Molde"
PROJECT_START = "2026-01-12T08:00:00"
PROJECT_FINISH = "2026-06-05T17:00:00"
CREATED = "2026-05-29T08:00:00"

# Predecessor type codes i MS Project XML:
#   0 = FF (Finish-to-Finish)
#   1 = FS (Finish-to-Start) — default
#   2 = SF (Start-to-Finish)
#   3 = SS (Start-to-Start)
PRED_TYPE = {"FF": 0, "FS": 1, "SF": 2, "SS": 3}

# ----- Aktiviteter -----
# Felter: (uid, navn, outline_level, summary?, milestone?,
#          start_date, finish_date, days, percent_complete, predecessors)
# predecessors: liste av (predecessor_uid, type_str, lag_dager)
ACTIVITIES = [
    # Fase 1 – Initiering -------------------------------------------------
    (1,  "Fase 1 – Initiering",                              1, True,  False, "2026-01-12", "2026-02-23", 31, 100, []),
    (2,  "ACT-01 Prosjektoppstart",                          2, False, False, "2026-01-12", "2026-01-19",  6, 100, []),
    (3,  "ACT-02 Utarbeidelse av proposal",                  2, False, False, "2026-01-12", "2026-02-23", 31, 100, [(2, "SS", 0)]),
    (4,  "M-01 Godkjent proposal",                           2, False, True,  "2026-02-23", "2026-02-23",  0, 100, [(3, "FS", 0)]),

    # Fase 2 – Planlegging ------------------------------------------------
    (5,  "Fase 2 – Planlegging",                             1, True,  False, "2026-02-16", "2026-03-19", 24, 100, []),
    (6,  "ACT-03 Litteraturgjennomgang",                     2, False, False, "2026-02-24", "2026-03-16", 15, 100, [(4, "FS", 0)]),
    (7,  "ACT-04 Metode og analyseopplegg",                  2, False, False, "2026-02-24", "2026-03-09", 10, 100, [(4, "FS", 0)]),
    (8,  "ACT-05 Prosjektplanlegging (WBS og Gantt)",        2, False, False, "2026-02-24", "2026-03-09", 10, 100, [(4, "FS", 0)]),
    (9,  "M-02 Godkjent prosjektplan",                       2, False, True,  "2026-03-09", "2026-03-09",  0, 100, [(8, "FS", 0)]),
    (10, "ACT-06 Datainnhenting fra REMA",                   2, False, False, "2026-02-16", "2026-03-19", 24, 100, []),

    # Fase 3 – Gjennomføring (analyse og modellering) --------------------
    (11, "Fase 3 – Gjennomføring",                           1, True,  False, "2026-02-16", "2026-05-04", 56, 100, []),
    (12, "ACT-07 Datavask og strukturering",                 2, False, False, "2026-02-16", "2026-04-15", 43, 100, [(10, "SS", 0)]),
    (13, "ACT-08 Analyse og modellering",                    2, False, False, "2026-03-16", "2026-04-16", 24, 100, [(12, "SS", 20)]),
    (14, "M-03 Ferdig analyse",                              2, False, True,  "2026-04-16", "2026-04-16",  0, 100, [(13, "FS", 0)]),
    (15, "ACT-09 Skriving av metode og resultat",            2, False, False, "2026-03-10", "2026-04-27", 35, 100, [(9, "FS", 0)]),
    (16, "ACT-10 Peer review og kvalitetssikring",           2, False, False, "2026-04-27", "2026-05-04",  5, 100, [(14, "FS", 0), (15, "FS", 0)]),
    (17, "M-05 Peer review gjennomført",                     2, False, True,  "2026-05-04", "2026-05-04",  0, 100, [(16, "FS", 0)]),

    # Fase 4 – Avslutning og innlevering ---------------------------------
    (18, "Fase 4 – Avslutning og innlevering",               1, True,  False, "2026-05-04", "2026-06-05", 25, 30,  []),
    (19, "ACT-11 Ferdigstillelse av rapportutkast",          2, False, False, "2026-05-04", "2026-05-18", 11, 95,  [(17, "FS", 0)]),
    (20, "M-04 Hovedutkast ferdig",                          2, False, True,  "2026-05-18", "2026-05-18",  0, 100, [(19, "FS", 0)]),
    (21, "ACT-12 Endelig revisjon og innlevering",           2, False, False, "2026-05-19", "2026-05-29",  9, 30,  [(20, "FS", 0)]),
    (22, "M-06 Ferdig kvalitetssikret rapport",              2, False, True,  "2026-05-31", "2026-05-31",  0, 0,   [(21, "FS", 0)]),
    (23, "ACT-13 Eksamensforberedelser",                     2, False, False, "2026-06-01", "2026-06-05",  5, 0,   [(22, "FS", 0)]),
    (24, "M-07 Gjennomført muntlig eksamen",                 2, False, True,  "2026-06-05", "2026-06-05",  0, 0,   [(23, "FS", 0)]),
]

# ----- Hjelpere -----
def fmt_dur(days):
    """ISO 8601-duration i timer (8t pr arbeidsdag)."""
    if isinstance(days, int):
        hours = days * 8
    else:
        hours = round(days * 8)
    return f"PT{hours}H0M0S"

def fmt_start(date_str):
    return f"{date_str}T08:00:00"

def fmt_finish(date_str, is_milestone=False):
    # Milepæler har Start = Finish på samme klokkeslett
    return f"{date_str}T08:00:00" if is_milestone else f"{date_str}T17:00:00"

def xml_escape(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&apos;"))

# ----- Bygg kalender -----
def build_calendar():
    """Standard 5-dagers kalender, 08:00-12:00 + 13:00-17:00."""
    work_block = """          <WorkingTimes>
            <WorkingTime>
              <FromTime>08:00:00</FromTime>
              <ToTime>12:00:00</ToTime>
            </WorkingTime>
            <WorkingTime>
              <FromTime>13:00:00</FromTime>
              <ToTime>17:00:00</ToTime>
            </WorkingTime>
          </WorkingTimes>"""
    days_xml = []
    # DayType: 1=søn, 2=man, 3=tir, 4=ons, 5=tor, 6=fre, 7=lør
    for day_type in range(1, 8):
        if day_type in (1, 7):  # søndag og lørdag = fri
            days_xml.append(f"""        <WeekDay>
          <DayType>{day_type}</DayType>
          <DayWorking>0</DayWorking>
        </WeekDay>""")
        else:
            days_xml.append(f"""        <WeekDay>
          <DayType>{day_type}</DayType>
          <DayWorking>1</DayWorking>
{work_block}
        </WeekDay>""")
    weekdays = "\n".join(days_xml)
    return f"""  <Calendars>
    <Calendar>
      <UID>1</UID>
      <Name>Standard</Name>
      <IsBaseCalendar>1</IsBaseCalendar>
      <BaseCalendarUID>-1</BaseCalendarUID>
      <WeekDays>
{weekdays}
      </WeekDays>
    </Calendar>
  </Calendars>"""

# ----- Bygg en task -----
def build_task(activity):
    (uid, name, outline_level, is_summary, is_milestone,
     start_d, finish_d, days, pct, predecessors) = activity

    name_esc = xml_escape(name)
    start = fmt_start(start_d)
    finish = fmt_finish(finish_d, is_milestone)
    duration = fmt_dur(days)
    summary = 1 if is_summary else 0
    milestone = 1 if is_milestone else 0

    actual_start = start if pct > 0 else "NA"
    actual_finish = finish if pct == 100 else "NA"
    actual_duration = fmt_dur(days * pct / 100) if pct > 0 else "PT0H0M0S"
    remaining_duration = fmt_dur(days * (100 - pct) / 100)

    pred_xml = ""
    for pred_uid, pred_type, lag_days in predecessors:
        pred_code = PRED_TYPE[pred_type]
        lag_min = lag_days * 480  # 8t * 60 min
        pred_xml += f"""    <PredecessorLink>
      <PredecessorUID>{pred_uid}</PredecessorUID>
      <Type>{pred_code}</Type>
      <CrossProject>0</CrossProject>
      <LinkLag>{lag_min}</LinkLag>
      <LagFormat>7</LagFormat>
    </PredecessorLink>
"""

    return f"""  <Task>
    <UID>{uid}</UID>
    <ID>{uid}</ID>
    <Name>{name_esc}</Name>
    <Type>1</Type>
    <IsNull>0</IsNull>
    <CreateDate>{CREATED}</CreateDate>
    <OutlineLevel>{outline_level}</OutlineLevel>
    <Priority>500</Priority>
    <Start>{start}</Start>
    <Finish>{finish}</Finish>
    <Duration>{duration}</Duration>
    <DurationFormat>7</DurationFormat>
    <Work>PT0H0M0S</Work>
    <Stop>{start}</Stop>
    <Resume>{start}</Resume>
    <ResumeValid>0</ResumeValid>
    <EffortDriven>0</EffortDriven>
    <Recurring>0</Recurring>
    <OverAllocated>0</OverAllocated>
    <Estimated>0</Estimated>
    <Milestone>{milestone}</Milestone>
    <Summary>{summary}</Summary>
    <Critical>0</Critical>
    <IsSubproject>0</IsSubproject>
    <IsSubprojectReadOnly>0</IsSubprojectReadOnly>
    <ExternalTask>0</ExternalTask>
    <EarlyStart>{start}</EarlyStart>
    <EarlyFinish>{finish}</EarlyFinish>
    <LateStart>{start}</LateStart>
    <LateFinish>{finish}</LateFinish>
    <StartVariance>0</StartVariance>
    <FinishVariance>0</FinishVariance>
    <WorkVariance>0</WorkVariance>
    <CostVariance>0</CostVariance>
    <PercentComplete>{pct}</PercentComplete>
    <PercentWorkComplete>0</PercentWorkComplete>
    <Cost>0</Cost>
    <FixedCost>0</FixedCost>
    <FixedCostAccrual>3</FixedCostAccrual>
    <ActualStart>{actual_start}</ActualStart>
    <ActualFinish>{actual_finish}</ActualFinish>
    <ActualDuration>{actual_duration}</ActualDuration>
    <ActualCost>0</ActualCost>
    <ActualOvertimeCost>0</ActualOvertimeCost>
    <ActualWork>PT0H0M0S</ActualWork>
    <ActualOvertimeWork>PT0H0M0S</ActualOvertimeWork>
    <RegularWork>PT0H0M0S</RegularWork>
    <RemainingDuration>{remaining_duration}</RemainingDuration>
    <RemainingCost>0</RemainingCost>
    <RemainingWork>PT0H0M0S</RemainingWork>
    <RemainingOvertimeCost>0</RemainingOvertimeCost>
    <RemainingOvertimeWork>PT0H0M0S</RemainingOvertimeWork>
    <ACWP>0</ACWP>
    <CV>0</CV>
    <ConstraintType>0</ConstraintType>
    <CalendarUID>-1</CalendarUID>
    <ConstraintDate>NA</ConstraintDate>
    <Deadline>NA</Deadline>
    <LevelAssignments>1</LevelAssignments>
    <LevelingCanSplit>1</LevelingCanSplit>
    <LevelingDelay>0</LevelingDelay>
    <LevelingDelayFormat>8</LevelingDelayFormat>
    <PreLeveledStart>{start}</PreLeveledStart>
    <PreLeveledFinish>{finish}</PreLeveledFinish>
    <IgnoreResourceCalendar>0</IgnoreResourceCalendar>
    <PhysicalPercentComplete>0</PhysicalPercentComplete>
    <EarnedValueMethod>0</EarnedValueMethod>
    <Manual>1</Manual>
    <Active>1</Active>
{pred_xml}  </Task>
"""

# ----- Bygg hele XML-en -----
def build_xml():
    tasks_xml = "".join(build_task(a) for a in ACTIVITIES)
    calendar_xml = build_calendar()
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Project xmlns="http://schemas.microsoft.com/project">
  <SaveVersion>14</SaveVersion>
  <Name>{xml_escape(PROJECT_NAME)}</Name>
  <Title>{xml_escape(PROJECT_TITLE)}</Title>
  <Subject></Subject>
  <Category></Category>
  <Company>{xml_escape(PROJECT_COMPANY)}</Company>
  <Manager>{xml_escape(PROJECT_MANAGER)}</Manager>
  <Author>{xml_escape(PROJECT_AUTHOR)}</Author>
  <CreationDate>{CREATED}</CreationDate>
  <LastSaved>{CREATED}</LastSaved>
  <ScheduleFromStart>1</ScheduleFromStart>
  <StartDate>{PROJECT_START}</StartDate>
  <FinishDate>{PROJECT_FINISH}</FinishDate>
  <FYStartDate>1</FYStartDate>
  <CriticalSlackLimit>0</CriticalSlackLimit>
  <CurrencyDigits>2</CurrencyDigits>
  <CurrencySymbol>kr</CurrencySymbol>
  <CurrencySymbolPosition>1</CurrencySymbolPosition>
  <CalendarUID>1</CalendarUID>
  <DefaultStartTime>08:00</DefaultStartTime>
  <DefaultFinishTime>17:00</DefaultFinishTime>
  <MinutesPerDay>480</MinutesPerDay>
  <MinutesPerWeek>2400</MinutesPerWeek>
  <DaysPerMonth>20</DaysPerMonth>
  <DefaultTaskType>0</DefaultTaskType>
  <DefaultFixedCostAccrual>3</DefaultFixedCostAccrual>
  <DefaultStandardRate>0</DefaultStandardRate>
  <DefaultOvertimeRate>0</DefaultOvertimeRate>
  <DurationFormat>7</DurationFormat>
  <WorkFormat>2</WorkFormat>
  <EditableActualCosts>0</EditableActualCosts>
  <HonorConstraints>0</HonorConstraints>
  <InsertedProjectsLikeSummary>1</InsertedProjectsLikeSummary>
  <MultipleCriticalPaths>0</MultipleCriticalPaths>
  <NewTasksEffortDriven>0</NewTasksEffortDriven>
  <NewTasksEstimated>1</NewTasksEstimated>
  <SplitsInProgressTasks>1</SplitsInProgressTasks>
  <SpreadActualCost>0</SpreadActualCost>
  <SpreadPercentComplete>0</SpreadPercentComplete>
  <TaskUpdatesResource>1</TaskUpdatesResource>
  <FiscalYearStart>0</FiscalYearStart>
  <WeekStartDay>1</WeekStartDay>
  <MoveCompletedEndsBack>0</MoveCompletedEndsBack>
  <MoveRemainingStartsBack>0</MoveRemainingStartsBack>
  <MoveRemainingStartsForward>0</MoveRemainingStartsForward>
  <MoveCompletedEndsForward>0</MoveCompletedEndsForward>
  <BaselineForEarnedValue>0</BaselineForEarnedValue>
  <FiscalYearStartMonth>1</FiscalYearStartMonth>
  <NewTaskStartDate>0</NewTaskStartDate>
  <DefaultTaskEVMethod>0</DefaultTaskEVMethod>
  <ProjectExternallyEdited>0</ProjectExternallyEdited>
  <ExtendedCreationDate>{CREATED}</ExtendedCreationDate>
  <ActualsInSync>0</ActualsInSync>
  <RemoveFileProperties>0</RemoveFileProperties>
  <AdminProject>0</AdminProject>
{calendar_xml}
  <Tasks>
{tasks_xml}  </Tasks>
  <Resources/>
  <Assignments/>
</Project>
"""

def main():
    output = Path(__file__).parent / "Prosjektplan_G27_oppdatert.xml"
    xml_content = build_xml()
    output.write_text(xml_content, encoding="utf-8")
    print(f"Skrev {len(xml_content):,} tegn til {output.name}")
    print(f"Antall aktiviteter: {len(ACTIVITIES)}")

    # Verifiser at XML-en parser
    import xml.etree.ElementTree as ET
    try:
        ET.parse(output)
        print("OK: XML er well-formed")
    except ET.ParseError as e:
        print(f"FEIL: XML er ikke well-formed: {e}")
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
