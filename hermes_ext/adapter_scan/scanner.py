from __future__ import annotations

from hermes_ext.adapter_scan.ast_scanner import PythonASTScanner
from hermes_ext.adapter_scan.contracts import (
    AdapterIntegrationPosture,
    AdapterScanConfig,
    AdapterScanReport,
    AdapterScanSummary,
)
from hermes_ext.adapter_scan.extension_points import ExtensionPointMapper
from hermes_ext.adapter_scan.filesystem import ReadOnlyProjectFilesystem


class AdapterScanEngine:
    """
    High-level read-only scan engine.

    It scans Python files, maps extension points, and returns a report.
    It does not import scanned modules.
    """

    def __init__(self, config: AdapterScanConfig) -> None:
        self.config = config
        self.filesystem = ReadOnlyProjectFilesystem(config)
        self.ast_scanner = PythonASTScanner(config)
        self.mapper = ExtensionPointMapper()

    def run(self) -> AdapterScanReport:
        paths = self.filesystem.iter_source_files()
        records = [self.ast_scanner.scan_file(path) for path in paths]
        candidates = self.mapper.map_records(records)

        summary = AdapterScanSummary(
            files_scanned=len(records),
            lifeline_files_found=sum(1 for record in records if record.is_lifeline),
            candidates_found=len(candidates),
            forbidden_candidates=sum(
                1 for candidate in candidates
                if candidate.posture == AdapterIntegrationPosture.FORBIDDEN
            ),
            wrapper_only_candidates=sum(
                1 for candidate in candidates
                if candidate.posture == AdapterIntegrationPosture.WRAPPER_ONLY
            ),
            feature_flag_candidates=sum(
                1 for candidate in candidates
                if candidate.posture == AdapterIntegrationPosture.FEATURE_FLAG_REQUIRED
            ),
            parse_errors=sum(1 for record in records if record.parse_error is not None),
        )

        warnings: list[str] = []
        if summary.parse_errors:
            warnings.append(f"{summary.parse_errors} files had parse errors")
        if summary.forbidden_candidates:
            warnings.append(
                f"{summary.forbidden_candidates} forbidden candidates detected; these are mapping-only"
            )

        return AdapterScanReport(
            project_root=str(self.config.project_root),
            summary=summary,
            files=records,
            candidates=candidates,
            warnings=warnings,
        )