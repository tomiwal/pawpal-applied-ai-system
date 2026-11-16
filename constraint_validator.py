class ConstraintValidator:
    """Validates that a schedule meets all constraints"""
    
    def validate_schedule(self, schedule, available_minutes):
        """
        Check if schedule is valid
        
        Args:
            schedule: Schedule object with tasks
            available_minutes: How many minutes the owner has
        
        Returns:
            Dictionary with 'valid' (bool) and 'issues' (list of problems)
        """
        issues = []
        
        # Check 1: Does schedule exceed available time?
        if schedule.get_total_duration() > available_minutes:
            issues.append(
                f"Schedule exceeds available time: "
                f"{schedule.get_total_duration()} > {available_minutes} minutes"
            )
        
        # Check 2: Are tasks unrealistically short/long?
        for task in schedule.tasks:
            if task.duration_minutes < 5:
                issues.append(
                    f"Task '{task.title}' is too short ({task.duration_minutes}m) - unrealistic"
                )
            if task.duration_minutes > 120:
                issues.append(
                    f"Task '{task.title}' is too long ({task.duration_minutes}m) - unrealistic"
                )
        
        # Return results
        return {
            "valid": len(issues) == 0,  # Valid if no issues found
            "issues": issues
        }